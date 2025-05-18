from src.server import create_server
import uvicorn

if __name__ == "__main__":
    app = create_server()
    uvicorn.run(app)