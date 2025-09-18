import os

from dotenv import dotenv_values

fastapi_env = os.getenv("FASTAPI_ENV", "dev")

config = {
    **dotenv_values(".env"),
    **dotenv_values(f".env.{fastapi_env}"),
    **os.environ,  # override loaded values with environment variables
}
