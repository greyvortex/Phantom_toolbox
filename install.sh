#!/bin/bash

# Define the source Python script name and the desired shortcut name
PYTHON_SCRIPT="PHM_Recon.py"
SHORTCUT_NAME="phm_recon"
INSTALL_DIR="/usr/local/bin"

# Ensure the script is run with root privileges (for /usr/local/bin access)
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root or with sudo."
  exit 1
fi

# 1. Make the Python file executable
echo "Making Python script executable..."
chmod +x "$PYTHON_SCRIPT"

# 2. Add a shebang line to the Python script (if not already present)
# This allows the system to know how to run the file directly
if ! grep -q "#!/usr/bin/env python3" "$PYTHON_SCRIPT"; then
  echo "Adding shebang to $PYTHON_SCRIPT..."
  sed -i '1i#!/usr/bin/env python3' "$PYTHON_SCRIPT"
fi

# Get the absolute path of the Python script
SCRIPT_PATH="$(pwd)/$PYTHON_SCRIPT"

# 3. Create a symbolic link in the installation directory
echo "Creating a symbolic link in $INSTALL_DIR..."
ln -sf "$SCRIPT_PATH" "$INSTALL_DIR/$SHORTCUT_NAME"

# 4. Verify installation
echo "Installation complete. You can now run your script using the command: $SHORTCUT_NAME"