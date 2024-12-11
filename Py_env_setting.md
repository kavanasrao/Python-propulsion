# **Step-By_Step Instruction for python installing on System**

## Windows:
**Step ! : Download Python**
- Go to the official Python website: https://www.python.org.
- Click on the Downloads tab and choose the version compatible with Windows (usually the latest stable release for your system is displayed).

**Step 2 : Run the Installer**
- Locate the downloaded .exe file and double-click to run it.
- In the setup screen, check the box for "Add Python to PATH" (this is important for running Python from the command line).
- Click Customize installation (optional) if you want to select specific features or install it in a custom location, otherwise click Install Now.

**Step 3 : To Verify the Installation**
- Open the Command Prompt (Win + R, type cmd and hit enter)
- Type (python --version) or python and press Enter
- You should see the installed Python version.

**Step 4 : Install pip**
- Check if pip is installed by running pip --version in the command prompt
- If not, you can install it by running:

            python -m ensurepip --upgrade


<hr>

## Mac_OS

**Step 1 : Install python**
- Mac_OS comes with Python 2.x pre-installed. Install Python 3 by:
    - Visiting https://www.python.org and downloading the latest version for Mac.
    - Running the installer file and following the instructions.
- Alternatively, USe Homebrew to install Python:
    - Install Homebrew by running in terminal 

                    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    - Install Python with Homebrew :

                    brew install python

**Step 2 : Verify Installation :**

- Check the Python version :

            python --version

- Check pip version :

            pip3 --version


<hr>

## Linux 

**Step 1 : Check pre_installed Python :**
- Open Terminal(clt + alt + T)
- Run the following command to check the installed version:

                python3 --version

**Step 2 : Install Python**

- Update your package list:

                sudo apt update

- Install Python 

                sudo apt install python3 python3-pip

- For other distributions, use te package manager(yum,dnf, etc) to install python


**Step 3 : Verify Installation**

- Check Python version :

                python3 --version

- Check pip version :

                pip3 --version





