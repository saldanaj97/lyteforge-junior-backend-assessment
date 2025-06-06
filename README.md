# LyteForge Junior Backend Assessment - CRUD Application

A full-stack CRUD application built with FastAPI and MongoDB, featuring geospatial search capabilities and JWT authentication.

## Features

- **Authentication**: JWT-based admin authentication
- **CRUD Operations**: Create, Read, Update, Delete items
- **Geospatial Search**: Find items within a specified radius (not working)
- **Web Interface**: Simple HTML/CSS/JS frontend
- **Docker Support**: Containerized deployment

## Prerequisites

- Docker
- Docker Compose
- Git

## Quick Start with Docker

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd lyteforge-junior-backend-assessment
   ```

2. **Create environment file**
   For the purpose of this assessment, I have included the .env with test credentials since we are running this in docker and so it's easier to clone and run the docker commands but I am aware NOT to do this in production.

3. **Build and run with Docker**

   ```bash
    docker compose up ---build
   ```

4. **Access the application**
   - Open your browser and go to: `http://localhost:8000`
   - Use the demo credentials to login:
     - Username: `admin`
     - Password: `admin123`

## API Endpoints

### Authentication

- `POST /auth/login` - Login with admin credentials
- `POST /auth/logout` - Logout (client-side token removal)

### Items CRUD

- `GET /items/` - Get all items
- `POST /items/` - Create new item
- `GET /items/{id}` - Get item by ID
- `PUT /items/{id}` - Update item
- `DELETE /items/{id}` - Delete item
- `GET /items/search` - Search items by location

## Usage

### Login

1. Navigate to `http://localhost:8000`
2. Use the provided demo credentials:
   - Username: `admin`
   - Password: `admin123`

### Creating Items

Items require the following fields:

- **Name**: String identifier
- **Description**: Text description
- **Longitude**: Geographic longitude (-180 to 180)
- **Latitude**: Geographic latitude (-90 to 90)

### Geospatial Search

Search for items within a radius:

1. Enter center coordinates (longitude, latitude)
2. Specify radius in meters
3. Click "Search" to find nearby items

### Project Structure

```
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── core/
│   │   └── database.py      # MongoDB connection
│   └── api/
│       └── routes/
│           ├── auth.py      # Authentication endpoints
│           └── items.py     # CRUD endpoints
├── static/
│   ├── index.html          # Frontend interface
│   └── styles.css          # Styling
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Environment Variables

For the purpose of this assessment, I have included a .env so its easier to clone and run the docker commands but doing this NOT safe for production.

| Variable        | Description               | Default  |
| --------------- | ------------------------- | -------- |
| `MONGO_URI`     | MongoDB connection string | Required |
| `MONGO_DB_NAME` | Database name             | Required |

## Troubleshooting

### Common Issues

1. **Connection refused**: Ensure MongoDB is running and accessible
2. **Authentication failed**: Check if credentials are correct (admin/admin123)
3. **Port conflicts**: Make sure port 8000 is available

## Technology Stack

- **Backend**: FastAPI (Python)
- **Database**: MongoDB with geospatial indexing
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Authentication**: JWT tokens
- **Containerization**: Docker
