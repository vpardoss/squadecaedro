#!/bin/bash
# ARCHIVO HECHO CON IA
# A simple script to replace all colons (:) with hyphens (-)
# in the filenames of the current directory.

echo "Starting file renaming process..."

# Loop through every file in the current directory
for old_name in *; do
    
    # Check if the item is actually a file before proceeding
    if [ -f "$old_name" ]; then

        # Create the new name by replacing all colons with hyphens
        # This uses bash's built-in string replacement for efficiency
        new_name="${old_name//:/-}"

        # Only rename if the new name is different from the old name
        if [ "$old_name" != "$new_name" ]; then
            
            # Use "mv" to perform the rename
            mv "$old_name" "$new_name"
            
            # Print a confirmation message
            echo "Renamed: '$old_name' -> '$new_name'"
        fi
    fi
done

echo "Renaming process complete."
