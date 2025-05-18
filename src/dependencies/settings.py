from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    twilio_account_sid: str = ""
    twilio_auth_token: str = ""

    model_config = SettingsConfigDict(
        env_file=".env"
        
    )

def get_settings():
    return AppSettings()