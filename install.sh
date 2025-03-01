#!/bin/bash

echo "Welcome to the Port Scanner installation script!"
echo "This script will help you install the Port Scanner program from GitHub."
echo ""

read -p "Do you want to install Port Scanner for terminal use? (y/n): " install_choice

if [[ "$install_choice" == "y" || "$install_choice" == "Y" ]]; then
    echo "You chose to install the program."

    echo "Checking for Python 3 and pip..."

    if command -v python3 &>/dev/null && command -v pip &>/dev/null; then
        echo "Python 3 and pip are installed."
    else
        echo "Python 3 or pip is missing. Please install Python 3 and pip before proceeding."
        exit 1
    fi

    echo "Installing required Python modules..."

    echo "Cloning the Port Scanner repository from GitHub..."
    git clone https://github.com/bob-and-alice/port.git

    cd port || exit

    pip install -r requirements.txt

    echo "Installation complete!"
    echo "To run the program, use the following command: python3 port.py"
    
    read -p "Do you want to make the script executable from anywhere in the terminal? (y/n): " executable_choice

    if [[ "$executable_choice" == "y" || "$executable_choice" == "Y" ]]; then
        echo "Making the script executable..."

        sudo cp port.py /usr/bin/port
        sudo chmod +x /usr/bin/port
        sudo sed -i '1s|^|#!/usr/bin/env python3\n|' /usr/bin/port

        echo "The script is now executable from anywhere. You can run it using the command: port"
    else
        echo "You can still run the program using: python3 port.py"
    fi

else
    echo "Installation canceled. Exiting..."
    exit 0
fi
