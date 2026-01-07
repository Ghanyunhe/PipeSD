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
    """Format API response.
    
    Args:
        data: The response data
        status: Response status (default: "success")
        
    Returns:
        Formatted response dictionary
        
    Raises:
        ValueError: If status is not a valid value
    """
    valid_statuses = {"success", "error", "pending", "warning"}
    if status not in valid_statuses:
        raise ValueError(f"Invalid status '{status}'. Must be one of {valid_statuses}")
    
    return {
        "status": status,
        "data": data
    }
