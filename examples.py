"""
PipeSD Example Usage

This example demonstrates how to use the edge and cloud services together.
"""

from edge.services.service_manager import EdgeServiceManager
from edge.api.handler import EdgeAPIHandler
from cloud.services.service_manager import CloudServiceManager
from cloud.api.handler import CloudAPIHandler


def example_edge_service():
    """Example of using edge services."""
    print("=== Edge Service Example ===")
    
    # Initialize edge service manager
    edge_manager = EdgeServiceManager()
    
    # Initialize edge API handler
    edge_api = EdgeAPIHandler()
    
    # Register a sample endpoint
    def hello_handler(data):
        return {"message": f"Hello from edge! Received: {data}"}
    
    edge_api.register_endpoint("/hello", hello_handler)
    
    # Test the endpoint
    response = edge_api.handle_request("/hello", {"name": "test"})
    print(f"Edge API Response: {response}")
    
    print("✓ Edge service initialized successfully\n")


def example_cloud_service():
    """Example of using cloud services."""
    print("=== Cloud Service Example ===")
    
    # Initialize cloud service manager
    cloud_manager = CloudServiceManager()
    
    # Initialize cloud API handler
    cloud_api = CloudAPIHandler()
    
    # Register a sample endpoint
    def process_handler(data):
        return {"result": f"Processed on cloud: {data}"}
    
    cloud_api.register_endpoint("/process", process_handler)
    
    # Register an edge device
    cloud_manager.register_edge("edge-device-001")
    
    # Test the endpoint
    response = cloud_api.handle_request("/process", {"data": "sample"})
    print(f"Cloud API Response: {response}")
    
    # List endpoints
    endpoints = cloud_api.list_endpoints()
    print(f"Available endpoints: {endpoints}")
    
    print("✓ Cloud service initialized successfully\n")


def example_edge_cloud_integration():
    """Example of edge-cloud integration."""
    print("=== Edge-Cloud Integration Example ===")
    
    # Edge side
    edge_manager = EdgeServiceManager()
    edge_api = EdgeAPIHandler()
    
    # Cloud side
    cloud_manager = CloudServiceManager()
    cloud_api = CloudAPIHandler()
    
    # Edge sends data to cloud
    def edge_send_data(data):
        # In real scenario, this would make HTTP request to cloud
        return cloud_api.handle_request("/ingest", data)
    
    # Cloud receives and processes data
    def cloud_ingest_handler(data):
        return {
            "status": "success",
            "message": f"Data received from edge",
            "processed_data": data
        }
    
    cloud_api.register_endpoint("/ingest", cloud_ingest_handler)
    
    # Simulate edge sending data
    edge_data = {"sensor": "temperature", "value": 25.5}
    result = edge_send_data(edge_data)
    
    print(f"Integration Result: {result}")
    print("✓ Edge-Cloud integration working\n")


if __name__ == "__main__":
    print("PipeSD Service Examples\n" + "="*50 + "\n")
    
    # Run examples
    example_edge_service()
    example_cloud_service()
    example_edge_cloud_integration()
    
    print("="*50)
    print("All examples completed successfully!")
