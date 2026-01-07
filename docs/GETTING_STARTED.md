# Getting Started with PipeSD

This guide will help you get started with PipeSD's edge and cloud services.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Ghanyunhe/PipeSD.git
cd PipeSD
```

2. (Optional) Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### Running the Examples

To see PipeSD in action, run the examples file:

```bash
python3 examples.py
```

This will demonstrate:
- Edge service initialization
- Cloud service initialization
- Edge-cloud integration

### Using Edge Services

```python
from edge.services.service_manager import EdgeServiceManager
from edge.api.handler import EdgeAPIHandler

# Initialize edge components
edge_manager = EdgeServiceManager()
edge_api = EdgeAPIHandler()

# Register an endpoint
def my_handler(data):
    return {"result": f"Processed: {data}"}

edge_api.register_endpoint("/process", my_handler)

# Handle a request
response = edge_api.handle_request("/process", {"value": 42})
print(response)
```

### Using Cloud Services

```python
from cloud.services.service_manager import CloudServiceManager
from cloud.api.handler import CloudAPIHandler

# Initialize cloud components
cloud_manager = CloudServiceManager()
cloud_api = CloudAPIHandler()

# Register an edge device
cloud_manager.register_edge("edge-device-001")

# Register an endpoint
def aggregate_handler(data):
    return {"status": "success", "data": data}

cloud_api.register_endpoint("/aggregate", aggregate_handler)

# Handle a request
response = cloud_api.handle_request("/aggregate", {"values": [1, 2, 3]})
print(response)
```

## Configuration

### Edge Configuration

Edit `edge/config.yaml` to configure edge services:

```yaml
service:
  name: "my-edge-service"
  port: 8080

connection:
  cloud_endpoint: "https://your-cloud-endpoint.com"
  timeout: 30
```

### Cloud Configuration

Edit `cloud/config.yaml` to configure cloud services:

```yaml
service:
  name: "my-cloud-service"
  port: 443

cloud:
  provider: "aws"
  region: "us-east-1"
```

## Project Structure

```
PipeSD/
├── edge/              # Edge computing components
├── cloud/             # Cloud service components
├── docs/              # Documentation
├── config/            # Shared configurations
├── examples.py        # Example usage
└── requirements.txt   # Python dependencies
```

## Next Steps

1. Read the [Architecture Documentation](docs/ARCHITECTURE.md)
2. Review the [Migration Documentation](docs/MIGRATION.md)
3. Explore the edge services in `edge/`
4. Explore the cloud services in `cloud/`
5. Customize configurations for your use case

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black .
```

### Type Checking

```bash
mypy edge/ cloud/
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure you're running from the repository root
2. **Configuration Errors**: Check YAML syntax in config files
3. **Connection Issues**: Verify network connectivity between edge and cloud

## Support

For issues and questions:
- Check the documentation in `docs/`
- Review the example code in `examples.py`
- Open an issue on GitHub

## License

(To be added)
