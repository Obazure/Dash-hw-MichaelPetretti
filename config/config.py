import os

STORAGE_DIRECTORY = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "storage"
    )
)
if not os.path.exists(STORAGE_DIRECTORY):
    os.makedirs(STORAGE_DIRECTORY)

APPLICATION_MODE_DEBUGABLE = os.getenv("DEBUG", True)