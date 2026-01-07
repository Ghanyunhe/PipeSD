"""
Edge Utilities

Common utility functions for edge operations.
"""

import logging

def setup_logging(level=logging.INFO):
    """Setup logging configuration for edge services."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def validate_config(config: dict) -> bool:
    """Validate edge service configuration."""
    required_keys = ['service_name', 'endpoint']
    return all(key in config for key in required_keys)
