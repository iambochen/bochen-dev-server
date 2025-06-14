from celery import shared_task
import time
import logging

logger = logging.getLogger(__name__)

@shared_task
async def add(x: int, y: int) -> int:
    """Example task that adds two numbers."""
    logger.info(f"Adding {x} + {y}")
    time.sleep(2)  # Simulate some work
    return x + y

@shared_task
async def multiply(x: int, y: int) -> int:
    """Example task that multiplies two numbers."""
    logger.info(f"Multiplying {x} * {y}")
    time.sleep(1)  # Simulate some work
    return x * y
