# PipeSD

PipeSD is a unified pipeline service deployment system that integrates edge and cloud computing capabilities.

## Project Structure

```
PipeSD/
├── edge/                 # Edge computing components
│   ├── services/        # Edge service implementations
│   ├── api/            # Edge API handlers
│   ├── utils/          # Edge utility functions
│   └── config.yaml     # Edge configuration
├── cloud/               # Cloud service components
│   ├── services/       # Cloud service implementations
│   ├── api/           # Cloud API handlers
│   ├── utils/         # Cloud utility functions
│   └── config.yaml    # Cloud configuration
├── docs/               # Documentation
└── config/             # Shared configuration files
```

## Components

### Edge Services
Edge services handle local data processing, device management, and communication with cloud services. They are designed to run on edge devices with limited resources while maintaining high performance and reliability.

### Cloud Services
Cloud services provide centralized data processing, storage, analytics, and management capabilities. They coordinate with edge services to provide a complete pipeline solution.

## Getting Started

### Prerequisites
- Python 3.8+
- Required dependencies (to be added)

### Installation
```bash
# Clone the repository
git clone https://github.com/Ghanyunhe/PipeSD.git
cd PipeSD

# Install dependencies
pip install -r requirements.txt  # (to be added)
```

### Configuration
- Edge configuration: `edge/config.yaml`
- Cloud configuration: `cloud/config.yaml`

## Development

### Edge Development
See [edge/README.md](edge/README.md) for edge-specific development guidelines.

### Cloud Development
See [cloud/README.md](cloud/README.md) for cloud-specific development guidelines.

## License
(To be added)

## Contributing
(To be added)