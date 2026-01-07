"""
Edge API Handler

This module provides API handlers for edge operations.
"""

from typing import Dict, Any

class EdgeAPIHandler:
    """Handles edge API requests."""
    
    def __init__(self):
        self.endpoints = {}
        
    def register_endpoint(self, path: str, handler):
        """Register an API endpoint."""
        self.endpoints[path] = handler
        
    def handle_request(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming API request."""
        if path in self.endpoints:
            return self.endpoints[path](data)
        return {"error": "Endpoint not found"}
