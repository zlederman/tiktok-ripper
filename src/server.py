from fastapi import FastAPI
from src.dependencies.settings import get_settings
from src.router.sms import sms_router

def create_server():
    settings = get_settings()
    for setting, value in settings.model_dump().items():
        assert value != ""; setting
    app = FastAPI()
    app.include_router(sms_router)
    return app

