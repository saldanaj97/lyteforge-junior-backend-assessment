from typing import List, Optional

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, Query

from app.api.routes.auth import verify_token
from app.api.schemas import ItemCreate, ItemResponse
from app.core.database import get_collection

router = APIRouter()
collection = get_collection("locations")

# Ensure 2dsphere index for geospatial queries
collection.create_index([("location", "2dsphere")])


@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, current_user: str = Depends(verify_token)):
    """Create a new geo-located item."""
    try:
        geo_item = {
            "name": item.name,
            "description": item.description,
            "location": {
                "type": "Point",
                "coordinates": [item.longitude, item.latitude],
            },
        }
        result = collection.insert_one(geo_item)
        return ItemResponse(
            id=str(result.inserted_id),
            name=item.name,
            description=item.description,
            longitude=item.longitude,
            latitude=item.latitude,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create item: {e}")


@router.get("/", response_model=List[ItemResponse])
def read_all_items(current_user: str = Depends(verify_token)):
    """Retrieve all items."""
    items = [
        ItemResponse(
            id=str(item["_id"]),
            name=item["name"],
            description=item.get("description"),
            longitude=item["location"]["coordinates"][0],
            latitude=item["location"]["coordinates"][1],
        )
        for item in collection.find()
    ]
    return items


@router.get("/{item_id}", response_model=ItemResponse)
def read_one_item(item_id: str, current_user: str = Depends(verify_token)):
    """Retrieve a single item by its ID."""
    try:
        object_id = ObjectId(item_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid item ID format")

    item = collection.find_one({"_id": object_id})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return ItemResponse(
        id=str(item["_id"]),
        name=item["name"],
        description=item.get("description"),
        longitude=item["location"]["coordinates"][0],
        latitude=item["location"]["coordinates"][1],
    )


@router.put("/{item_id}")
def update_one_item(
    item_id: str, item: ItemCreate, current_user: str = Depends(verify_token)
):
    """Update an existing item by its ID."""
    try:
        object_id = ObjectId(item_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid item ID format")

    geo_item = {
        "name": item.name,
        "description": item.description,
        "location": {
            "type": "Point",
            "coordinates": [item.longitude, item.latitude],
        },
    }

    result = collection.update_one({"_id": object_id}, {"$set": geo_item})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"item_id": item_id, "status": "updated"}


@router.delete("/{item_id}")
def delete_one_item(item_id: str, current_user: str = Depends(verify_token)):
    """Delete an item by its ID."""
    try:
        object_id = ObjectId(item_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid item ID format")

    result = collection.delete_one({"_id": object_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"item_id": item_id, "status": "deleted"}


@router.get("/search", response_model=List[ItemResponse])
def search_items_nearby(
    latitude: float = Query(
        ..., ge=-90, le=90, description="Latitude between -90 and 90"
    ),
    longitude: float = Query(
        ..., ge=-180, le=180, description="Longitude between -180 and 180"
    ),
    radius: Optional[int] = Query(
        1000, ge=1, description="Max search radius in meters"
    ),
    current_user: str = Depends(verify_token),
):
    """Search for items near a given location within an optional radius."""
    try:
        query = {
            "location": {
                "$near": {
                    "$geometry": {
                        "type": "Point",
                        "coordinates": [longitude, latitude],
                    },
                    "$maxDistance": radius,
                }
            }
        }
        results = collection.find(query).limit(50)
        return [
            ItemResponse(
                id=str(item["_id"]),
                name=item["name"],
                description=item.get("description"),
                longitude=item["location"]["coordinates"][0],
                latitude=item["location"]["coordinates"][1],
            )
            for item in results
        ]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search error: {e}")
