"""
Edge Service Manager

This module manages edge services and their lifecycle.
"""

class EdgeServiceManager:
    """Manages edge services and device connections."""
    
    def __init__(self):
        self.services = {}
        
    def register_service(self, service_name, service_instance):
        """Register a new edge service."""
        self.services[service_name] = service_instance
        
    def start_service(self, service_name):
        """Start a registered edge service."""
        if service_name in self.services:
            self.services[service_name].start()
            
    def stop_service(self, service_name):
        """Stop a running edge service."""
        if service_name in self.services:
            self.services[service_name].stop()
