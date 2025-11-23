# FastAPI React Boilerplate

A minimal full-stack web application boilerplate for quick Proof-of-Concept development.

## Tech Stack

- **Backend:** Python FastAPI with SQLite database
- **Frontend:** React with TypeScript
- **Authentication:** Session-based with HTTP-only cookies
- **Containerization:** Docker Compose

## Features

- Session-based authentication (no JWT)
- User registration and login
- Protected routes
- Basic user CRUD operations
- Password hashing with bcrypt
- SQLAlchemy ORM
- CORS configured
- Hot reload for development

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── api/          # API endpoints
│   │   ├── core/         # Security and dependencies
│   │   ├── db/           # Database configuration
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # Pydantic schemas
│   │   └── main.py       # FastAPI application
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── contexts/     # Auth context
│   │   ├── pages/        # Page components
│   │   ├── services/     # API services
│   │   ├── types/        # TypeScript types
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── Dockerfile
│   ├── Dockerfile.dev
│   ├── nginx.conf
│   └── package.json
├── docker-compose.yml
├── docker-compose.dev.yml
└── README.md
```

## Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Git

### Development Setup (with Hot Reload)

1. Clone the repository:
```bash
git clone <repository-url>
cd boilerplate-react-python
```

2. Start the development environment:
```bash
docker-compose -f docker-compose.dev.yml up --build
```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Production Setup

1. Build and start the containers:
```bash
docker-compose up --build
```

2. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000

## API Endpoints

### Authentication

- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and create session
- `POST /auth/logout` - Logout and clear session
- `GET /auth/me` - Get current user (protected)

### Users

- `GET /users/` - Get all users (protected)
- `GET /users/{id}` - Get user by ID (protected)
- `DELETE /users/{id}` - Delete user (protected)

## Development

### Backend Development

The backend uses FastAPI with hot reload enabled in development mode. Any changes to Python files will automatically restart the server.

### Frontend Development

The frontend uses Create React App with hot reload. Changes to React components will be reflected immediately.

### Database

SQLite database file (`app.db`) is created automatically on first run. It's stored in the backend volume.

## Environment Variables

### Backend

- `PYTHONUNBUFFERED=1` - Ensures Python output is sent straight to terminal

### Frontend

- `REACT_APP_API_URL` - Backend API URL (default: http://localhost:8000)
- `CHOKIDAR_USEPOLLING=true` - Enables hot reload in Docker

## Security Notes

- **Change the SECRET_KEY** in `backend/app/core/security.py` for production use
- Enable HTTPS and set `secure=True` for cookies in production
- Session tokens expire after 7 days
- Passwords are hashed using bcrypt

## Usage

### Register a New User

1. Navigate to http://localhost:3000/register
2. Enter email and password
3. Click "Register"

### Login

1. Navigate to http://localhost:3000/login
2. Enter credentials
3. Click "Login"

### Access Protected Routes

After logging in, you can access:
- Dashboard: http://localhost:3000/dashboard
- Users list: http://localhost:3000/users

## Stopping the Application

```bash
docker-compose down
```

Or for development:

```bash
docker-compose -f docker-compose.dev.yml down
```

## Clean Up

To remove all containers, volumes, and images:

```bash
docker-compose down -v --rmi all
```

## Customization

This boilerplate is designed to be minimal and easy to customize:

1. Add new models in `backend/app/models/`
2. Add new API endpoints in `backend/app/api/`
3. Add new React pages in `frontend/src/pages/`
4. Add new components in `frontend/src/components/`

## Troubleshooting

### Backend not starting
- Check if port 8000 is already in use
- Check logs: `docker-compose logs backend`

### Frontend not starting
- Check if port 3000 is already in use
- Check logs: `docker-compose logs frontend`

### Database issues
- Remove the volume and restart: `docker-compose down -v && docker-compose up`

### CORS issues
- Ensure the frontend URL is in the `allow_origins` list in `backend/app/main.py`

## License

See LICENSE file for details.
