"""
Cloud Service Manager

This module manages cloud services and their lifecycle.
"""

class CloudServiceManager:
    """Manages cloud services and connections."""
    
    def __init__(self):
        self.services = {}
        self.connected_edges = []
        
    def register_service(self, service_name, service_instance):
        """Register a new cloud service."""
        self.services[service_name] = service_instance
        
    def start_service(self, service_name):
        """Start a registered cloud service."""
        if service_name in self.services:
            service = self.services[service_name]
            if hasattr(service, 'start') and callable(service.start):
                service.start()
            else:
                raise AttributeError(f"Service {service_name} does not have a start method")
            
    def stop_service(self, service_name):
        """Stop a running cloud service."""
        if service_name in self.services:
            service = self.services[service_name]
            if hasattr(service, 'stop') and callable(service.stop):
                service.stop()
            else:
                raise AttributeError(f"Service {service_name} does not have a stop method")
            
    def register_edge(self, edge_id):
        """Register an edge device connection."""
        if edge_id not in self.connected_edges:
            self.connected_edges.append(edge_id)
