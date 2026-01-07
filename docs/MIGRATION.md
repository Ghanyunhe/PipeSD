# Migration Documentation

## Overview

This document describes the migration of edge and cloud repository contents into the unified PipeSD repository.

## Migration Date
January 7, 2026

## Repository Structure

The PipeSD repository now contains two main components that were previously in separate repositories:

### 1. Edge Repository Content
Located in: `edge/`

The edge repository content includes:
- **Services** (`edge/services/`): Edge service manager and related service implementations
- **API** (`edge/api/`): Edge API handlers for device communication
- **Utils** (`edge/utils/`): Common utility functions for edge operations
- **Configuration** (`edge/config.yaml`): Edge-specific configuration settings

### 2. Cloud Repository Content
Located in: `cloud/`

The cloud repository content includes:
- **Services** (`cloud/services/`): Cloud service manager and related service implementations
- **API** (`cloud/api/`): Cloud API handlers for centralized operations
- **Utils** (`cloud/utils/`): Common utility functions for cloud operations
- **Configuration** (`cloud/config.yaml`): Cloud-specific configuration settings

## Architecture

### Edge-Cloud Integration

```
┌─────────────────┐         ┌─────────────────┐
│   Edge Device   │ ◄─────► │  Cloud Service  │
│                 │         │                 │
│  - Services     │         │  - Services     │
│  - Local API    │         │  - Central API  │
│  - Processing   │         │  - Analytics    │
└─────────────────┘         └─────────────────┘
```

### Communication Flow

1. Edge devices process data locally
2. Edge services communicate with cloud via configured endpoints
3. Cloud services aggregate and analyze data from multiple edge devices
4. Cloud provides centralized management and monitoring

## Benefits of Consolidation

1. **Unified Codebase**: Easier maintenance and version control
2. **Shared Resources**: Common utilities and configurations
3. **Simplified Deployment**: Single repository for edge-cloud deployments
4. **Better Collaboration**: Developers can work on both components seamlessly

## Directory Guidelines

### Edge Directory (`edge/`)
- Contains all edge-specific code
- Focuses on local processing and device management
- Lightweight and optimized for edge devices

### Cloud Directory (`cloud/`)
- Contains all cloud-specific code
- Focuses on centralized processing and management
- Scalable and optimized for cloud infrastructure

### Shared Resources
- Common configurations can be placed in `config/`
- Shared documentation in `docs/`

## Future Enhancements

- [ ] Add shared library for common edge-cloud communication protocols
- [ ] Implement automated deployment scripts
- [ ] Add comprehensive test suites
- [ ] Create CI/CD pipelines for both edge and cloud components
- [ ] Add monitoring and logging infrastructure
