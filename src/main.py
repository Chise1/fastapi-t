import uvicorn
from realman import settings
from realman.factory import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app", port=8000, debug=settings.DEBUG, reload=settings.DEBUG, lifespan="on"
    )
