#!/bin/bash

# Change to the source directory
cd /

# Debug: Show current directory and contents
# pwd
# echo "Directory contents:"
# ls -la

# Run the Python application
while true; do
    python src/app.py
    if [ $? -ne 3 ]; then
        break
    fi
    echo "Restarting application..."
done
