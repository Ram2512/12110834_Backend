import motor.motor_asyncio
from pydantic_settings import BaseSettings

# Load environment settings
class Settings(BaseSettings):
    MONGODB_URL: str

# Load environment variables from .env file
settings = Settings(_env_file='.env')

# Set up MongoDB connection
client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
database = client.task_db  # Use the database "task_db"
task_collection = database.get_collection("tasks")  # Get tasks collection
