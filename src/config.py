from pydantic_settings import BaseSettings, SettingsConfigDict


class Configs(BaseSettings):
    back_url: str
    bot_token: str
    vk_bot_token: str
    model_config = SettingsConfigDict(
        env_file="./.env",
        env_file_encoding="utf-8"
    )
