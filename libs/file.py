import os
import string
from pathlib import Path
from configuration import Config, WorkerConfig

def url(filename, subdir: str) -> str:
    """Get url file

    Args:
        filename: filename
        subdir: subdirectory

    Returns:
        str url
    """
    if not filename:
        return ""

    static_url = Config.STATIC_URL
    if subdir:
        static_url = static_url + "/" + subdir
    
    return static_url + "/" + filename

def path(filename: str, subdir: str) -> Path:
    """Get full file path

    Args:
        filename: filename
        subdir: subdirectory

    Returns:
        str full path
    """
    upload_dir = Path(WorkerConfig.STORAGE_PATH)
    if subdir:
        upload_dir = upload_dir / subdir

    return upload_dir / filename