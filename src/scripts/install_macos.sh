#!/bin/bash

# Function to print progress messages
function info {
    echo "[INFO] $1"
}

# Install Python 3.12.8
info "Installing Python 3.12.8..."
PYTHON_VERSION="3.12.8"
PYTHON_DMG="python-${PYTHON_VERSION}-macos11.pkg"
PYTHON_URL="https://www.python.org/ftp/python/${PYTHON_VERSION}/${PYTHON_DMG}"

# Download Python installer
curl -o "/tmp/${PYTHON_DMG}" "${PYTHON_URL}" --silent

# Install Python
sudo installer -pkg "/tmp/${PYTHON_DMG}" -target / > /dev/null 2>&1
if [ $? -eq 0 ]; then
    info "Python 3.12.8 installed successfully."
else
    echo "[ERROR] Python installation failed."
    exit 1
fi

# Clean up
rm "/tmp/${PYTHON_DMG}"

# Verify Python installation
info "Verifying Python installation..."
python3 --version

info "Python installation script completed successfully."
info "Building Porn Fetch!"

cd "${HOME}" || { echo "[ERROR] Failed to change directory to ${HOME}"; exit 1; }
git clone https://github.com/EchterAlsFake/Porn_Fetch
cd "Porn_Fetch"

python3 -m venv /tmp/.venv # This is needed, because Qt has some issues if the virtual environment is in the same directory, as there the script gets executed in
source /tmp/.venv/bin/activate
pip install -r requirements.txt
pyside6-deploy -c src/build/pysidedeploy_macOS.spec -f -v
deactivate
echo "Deleting the temporary created virtual environment..."
rm -rf /tmp/.venv
echo "Porn Fetch is now installed in $(pwd)/main.bin"

