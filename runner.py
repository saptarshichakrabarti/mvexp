#!/usr/bin/env python3
"""
Entry point script for running the multiverse workflow.

This script provides a command-line interface for executing the multiverse
multimodal data integration workflow.
"""

import sys
import os
from multiverse.main import main_workflow


if __name__ == "__main__":
    try:
        # Parse command-line arguments
        config_path = sys.argv[1] if len(sys.argv) > 1 else "config_alldatasets.json"
        
        # Check if configuration file exists
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        
        print(f"Starting workflow with config: {config_path}")
        
        # Execute the main workflow
        main_workflow(config_path)
        
        print("Workflow completed successfully")
        
    except FileNotFoundError as e:
        print(f"CRITICAL EXECUTION ERROR: {e}", file=sys.stderr)
        print("Please provide a valid configuration file path.", file=sys.stderr)
        sys.exit(1)
        
    except Exception as e:
        print(f"CRITICAL EXECUTION ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
