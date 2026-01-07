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
            service = self.services[service_name]
            if hasattr(service, 'start') and callable(service.start):
                service.start()
            else:
                raise AttributeError(f"Service {service_name} does not have a start method")
            
    def stop_service(self, service_name):
        """Stop a running edge service."""
        if service_name in self.services:
            service = self.services[service_name]
            if hasattr(service, 'stop') and callable(service.stop):
                service.stop()
            else:
                raise AttributeError(f"Service {service_name} does not have a stop method")
