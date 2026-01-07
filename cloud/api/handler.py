"""
Cloud API Handler

This module provides API handlers for cloud operations.
"""

from typing import Dict, Any, List

class CloudAPIHandler:
    """Handles cloud API requests."""
    
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
        
    def list_endpoints(self) -> List[str]:
        """List all registered endpoints."""
        return list(self.endpoints.keys())
