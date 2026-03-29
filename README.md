# Library Application

A full-stack library management application built with React (frontend) and FastAPI (backend).

## Features

- Browse and manage books
- Track reading progress
- Add new books to collection

## Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd library-app/backend
   ```

2. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```

6. Add your API keys and configuration to `.env`:
   ```
   DATABASE_URL=sqlite:///./library.db
   SECRET_KEY=your-secret-key-here
   ```

7. Run the server:
   ```bash
   python -m uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd library-app/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```

4. Update the API URL in `.env` if needed:
   ```
   REACT_APP_API_URL=http://localhost:8000
   ```

5. Start the development server:
   ```bash
   npm start
   ```

The application will open at `http://localhost:3000`

## API Documentation

Once the backend is running, view the interactive API docs at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Environment Variables

See `.env.example` files in both backend and frontend directories for required environment variables.

**Important:** Never commit actual `.env` files or `secrets.txt` to version control. Use `.env.example` as a template.

## Deployment

### Hosting Options

- **Frontend**: Vercel, Netlify, or GitHub Pages
- **Backend**: Heroku, Railway, Render, AWS, or DigitalOcean
- **Database**: PostgreSQL (for production), SQLite (for development)

For deployment instructions, refer to your chosen hosting provider's documentation.

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]
