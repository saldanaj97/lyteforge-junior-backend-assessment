from fastapi import APIRouter

router = APIRouter()


@router.post("/{item_id}")
async def create_item(item_id: str):
    return {"item_id": item_id, "status": "created"}


@router.get("/")
async def read_all_items():
    return [{"item_id": "Foo"}, {"item_id": "Bar"}, {"item_id": "Baz"}]


@router.get("/{item_id}")
async def read_one_item(item_id: str):
    return {"item_id": item_id}


@router.put("/{item_id}")
async def update_one_item(item_id: str):
    return {"item_id": item_id}


@router.delete("/{item_id}")
async def delete_one_item(item_id: str):
    return {"item_id": item_id, "status": "deleted"}
