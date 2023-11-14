from app.utils.general import get_env_value


class Settings:
    POSTGRES_USER: str = get_env_value("POSTGRES_USER")
    POSTGRES_PASSWORD: str = get_env_value("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = get_env_value("POSTGRES_HOST")
    POSTGRES_PORT: str = get_env_value("POSTGRES_PORT")
    POSTGRES_DB: str = get_env_value("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
