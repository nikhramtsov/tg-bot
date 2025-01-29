from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    PG_DATABASE: str
    PG_USER: str
    PG_PASSWORD: str
    PG_HOST: str
    PG_PORT: str

    model_config = SettingsConfigDict(
        env_file='../.env',
        env_file_encoding='utf-8',
    )


settings = Settings()
