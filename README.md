# 🔄 JSON to YAML Converter

A simple Python utility for converting JSON files to YAML format with automatic filename matching and batch processing capabilities.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![PyYAML](https://img.shields.io/badge/PyYAML-6.0+-green.svg)](https://pyyaml.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Examples](#examples)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- 🎯 **Single File Conversion** - Convert individual JSON files to YAML
- 📦 **Batch Processing** - Convert multiple JSON files at once
- 🔄 **Auto Filename Matching** - Automatically generates YAML filename from JSON filename
- ⚡ **Overwrite Protection** - Safely overwrites existing YAML files
- 🛡️ **Error Handling** - Comprehensive error handling with detailed messages
- 🖥️ **CLI Interface** - Command-line interface for easy automation
- 🎨 **Custom Formatting** - Configurable YAML output formatting
- 📊 **Progress Reporting** - Real-time conversion status and statistics

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Install Dependencies

```bash
# Install required package
pip install PyYAML

# Or using requirements.txt
pip install -r requirements.txt
```

### Clone Repository

```bash
git clone https://github.com/jsnryhl/json-to-yaml-converter.git
cd json-to-yaml-converter
```

## 🏃 Quick Start

### Basic Usage

```python
from json_to_yaml import json_to_yaml

# Convert single file
json_to_yaml("config.json")  # Creates config.yaml
```

### Command Line

```bash
# Convert single file
python json_to_yaml.py config.json

# Batch convert all JSON files
python json_to_yaml.py --batch

# Batch convert in specific directory
python json_to_yaml.py --batch ./data/
```

## 📖 Usage

### Single File Conversion

Convert individual JSON files to YAML format:

```python
import json_to_yaml

# Basic conversion
json_to_yaml("data.json")                    # Creates data.yaml

# Custom output filename
json_to_yaml("input.json", "output.yaml")   # Custom name

# Check conversion success
success = json_to_yaml("config.json")
if success:
    print("Conversion completed successfully!")
```

### Batch Processing

Convert multiple JSON files simultaneously:

```python
from json_to_yaml import batch_convert_json_to_yaml

# Convert all JSON files in current directory
converted = batch_convert_json_to_yaml()

# Convert files in specific directory
converted = batch_convert_json_to_yaml("./configs/")

# Convert with pattern matching
converted = batch_convert_json_to_yaml("./data/", "api_*.json")
```

### Custom Formatting

Customize YAML output format:

```python
from json_to_yaml import json_to_yaml_custom_format

# Custom formatting options
json_to_yaml_custom_format(
    "data.json",
    indent=4,           # 4-space indentation
    sort_keys=True,     # Sort keys alphabetically
    width=120,          # Line width limit
    explicit_start=True # Add --- at start
)
```

## 💡 Examples

### Example 1: Configuration File Conversion

**Input (config.json):**
```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "username": "admin",
    "ssl": true
  },
  "cache": {
    "type": "redis",
    "ttl": 3600
  },
  "features": ["auth", "api", "logging"],
  "debug": false
}
```

**Output (config.yaml):**
```yaml
database:
  host: localhost
  port: 5432
  username: admin
  ssl: true
cache:
  type: redis
  ttl: 3600
features:
- auth
- api
- logging
debug: false
```

### Example 2: API Response Conversion

**Input (api_response.json):**
```json
{
  "status": "success",
  "data": {
    "users": [
      {"id": 1, "name": "John Doe", "active": true},
      {"id": 2, "name": "Jane Smith", "active": false}
    ],
    "total": 2
  },
  "timestamp": "2025-09-04T01:02:00Z"
}
```

**Command:**
```bash
python json_to_yaml.py api_response.json
```

**Output (api_response.yaml):**
```yaml
status: success
data:
  users:
  - id: 1
    name: John Doe
    active: true
  - id: 2
    name: Jane Smith
    active: false
  total: 2
timestamp: '2025-09-04T01:02:00Z'
```

### Example 3: Batch Conversion

```bash
# Directory structure
./data/
├── config.json
├── users.json
├── settings.json
└── metadata.json

# Convert all JSON files
python json_to_yaml.py --batch ./data/

# Result
./data/
├── config.json    → config.yaml
├── users.json     → users.yaml  
├── settings.json  → settings.yaml
└── metadata.json  → metadata.yaml
```

## 📚 API Reference

### `json_to_yaml(json_file_path, yaml_file_path=None)`

Convert a single JSON file to YAML format.

**Parameters:**
- `json_file_path` (str): Path to input JSON file
- `yaml_file_path` (str, optional): Custom output path. If None, uses same name with .yaml extension

**Returns:**
- `bool`: True if conversion successful, False otherwise

**Example:**
```python
success = json_to_yaml("data.json", "output.yaml")
```

### `batch_convert_json_to_yaml(directory=".", pattern="*.json")`

Convert multiple JSON files in a directory.

**Parameters:**
- `directory` (str): Directory to search for JSON files (default: current directory)
- `pattern` (str): File pattern to match (default: "*.json")

**Returns:**
- `List[str]`: List of successfully converted file paths

**Example:**
```python
converted = batch_convert_json_to_yaml("./configs/", "config_*.json")
```

### `json_to_yaml_custom_format(json_file_path, **yaml_options)`

Convert JSON to YAML with custom formatting options.

**Parameters:**
- `json_file_path` (str): Path to input JSON file
- `**yaml_options`: PyYAML dump options

**Available YAML Options:**
- `indent` (int): Number of spaces for indentation (default: 2)
- `sort_keys` (bool): Sort dictionary keys (default: False)
- `width` (int): Maximum line width (default: 120)
- `explicit_start` (bool): Add document start marker (default: True)
- `allow_unicode` (bool): Allow unicode characters (default: True)

## ⚙️ Configuration

### YAML Output Formatting

You can customize the YAML output format by modifying the default options:

```python
# Default YAML formatting options
DEFAULT_YAML_OPTIONS = {
    'default_flow_style': False,  # Use block style
    'allow_unicode': True,        # Support unicode
    'indent': 2,                  # 2-space indentation
    'sort_keys': False,           # Preserve key order
    'width': 120,                 # Line width limit
    'explicit_start': True        # Add --- marker
}
```

### Error Handling

The converter includes comprehensive error handling:

- **FileNotFoundError**: Input JSON file doesn't exist
- **JSONDecodeError**: Invalid JSON format
- **PermissionError**: Cannot write to output location
- **UnicodeError**: Character encoding issues

## 🔧 Development

### Running Tests

```bash
# Run unit tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=json_to_yaml tests/
```

### Code Style

```bash
# Format code
black json_to_yaml.py

# Lint code
flake8 json_to_yaml.py
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone repository
git clone https://github.com/jsnryhl/json-to-yaml-converter.git
cd json-to-yaml-converter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [PyYAML](https://pyyaml.org/) - YAML parser and emitter for Python
- [Python](https://python.org) - The programming language that makes this possible

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/jsnryhl/json-to-yaml-converter/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/jsnryhl/json-to-yaml-converter/discussions)
- 📧 **Email**: your.email@example.com

## 📈 Changelog

### v1.0.0 (2025-09-04)
- Initial release
- Single file conversion
- Batch processing
- CLI interface
- Custom formatting options
- Comprehensive error handling

---

**Made with ❤️ by [JSNRYHL](https://github.com/jsnryhl)**
