import json
import yaml
import os
import sys
from pathlib import Path
from typing import List, Optional

def json_to_yaml(json_file_path: str, yaml_file_path: Optional[str] = None) -> bool:
    """
    Convert JSON file to YAML file.
    
    Args:
        json_file_path: Path to input JSON file
        yaml_file_path: Optional custom output path. If None, uses same name with .yaml extension
    
    Returns:
        bool: True if conversion successful, False otherwise
    """
    json_path = Path(json_file_path)
    
    # Determine output path
    if yaml_file_path:
        yaml_path = Path(yaml_file_path)
    else:
        yaml_path = json_path.with_suffix('.yaml')
    
    try:
        # Validate input file exists
        if not json_path.exists():
            print(f"❌ Error: JSON file '{json_path}' not found")
            return False
        
        # Read and parse JSON
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        # Create output directory if it doesn't exist
        yaml_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write YAML file (overwrites if exists)
        with open(yaml_path, 'w', encoding='utf-8') as yaml_file:
            yaml.dump(data, yaml_file, 
                     default_flow_style=False,
                     allow_unicode=True,
                     indent=2,
                     sort_keys=False)
        
        file_size = yaml_path.stat().st_size
        print(f"✅ Converted: {json_path.name} → {yaml_path.name} ({file_size} bytes)")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON Parse Error in '{json_path}': {e}")
        return False
    except PermissionError:
        print(f"❌ Permission Error: Cannot write to '{yaml_path}'")
        return False
    except Exception as e:
        print(f"❌ Unexpected error converting '{json_path}': {e}")
        return False

def batch_convert_json_to_yaml(directory: str = ".", pattern: str = "*.json") -> List[str]:
    """
    Convert all JSON files in a directory to YAML.
    
    Args:
        directory: Directory to search for JSON files
        pattern: File pattern to match (default: "*.json")
    
    Returns:
        List of successfully converted files
    """
    dir_path = Path(directory)
    json_files = list(dir_path.glob(pattern))
    
    if not json_files:
        print(f"🔍 No JSON files found in '{directory}' matching pattern '{pattern}'")
        return []
    
    print(f"🔄 Found {len(json_files)} JSON files to convert...")
    
    converted_files = []
    for json_file in json_files:
        if json_to_yaml(str(json_file)):
            converted_files.append(str(json_file))
    
    print(f"\n📊 Conversion Summary: {len(converted_files)}/{len(json_files)} files converted successfully")
    return converted_files

# CLI Interface
def main():
    """Command line interface for JSON to YAML conversion."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python json_to_yaml.py <json_file>           # Convert single file")
        print("  python json_to_yaml.py --batch [directory]   # Convert all JSON files in directory")
        return
    
    if sys.argv[1] == "--batch":
        directory = sys.argv[2] if len(sys.argv) > 2 else "."
        batch_convert_json_to_yaml(directory)
    else:
        json_file = sys.argv[1]
        json_to_yaml(json_file)

if __name__ == "__main__":
    main()
