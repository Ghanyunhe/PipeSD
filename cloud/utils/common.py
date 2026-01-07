"""
Cloud Utilities

Common utility functions for cloud operations.
"""

import logging
from typing import Dict, Any

def setup_logging(level=logging.INFO):
    """Setup logging configuration for cloud services."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def validate_config(config: dict) -> bool:
    """Validate cloud service configuration."""
    required_keys = ['service_name', 'region', 'endpoint']
    return all(key in config for key in required_keys)

def format_response(data: Any, status: str = "success") -> Dict[str, Any]:
    """Format API response."""
    return {
        "status": status,
        "data": data
    }
