# Basic Python Terminology 

**Python Interpreter**
- Definition: The Python interpreter is the program that reads and executes Python code. It can either run code interactively or execute Python scripts.
- Example: Running python script.py or using python in the terminal to interactively execute commands.



## Python extension: (.py)
    
    A file extension is a small ending part of a file's name that tells the computer what kind of the file it is 


**pip (Python Package Installer)**
- Definition: pip is the package manager for Python. It allows you to install, update, and remove Python packages from the Python Package Index (PyPI).
- Example: Installing the requests package:

                pip install requests

<hr>

**Virtual Environment**
- Definition: A virtual environment is a self-contained directory that contains its own Python binary and libraries, allowing you to install and manage dependencies separately for each project.
- Why it's important: Prevents conflicts between different projects’ dependencies and allows you to manage project-specific libraries.
- Example: Creating a virtual environment:

                python -m venv myenv

Activating the virtual environment:

- On Windows: .\myenv\Scripts\activate
- On macOS/Linux: source myenv/bin/activate