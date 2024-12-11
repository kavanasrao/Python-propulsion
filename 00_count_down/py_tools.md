# **Development Tools Instructions**

## 1. Visual Studio Code(VS Code) * recommended*
VS Code is a lightweight but powerful source code editor from Microsoft, highly customizable, and supports Python development.

**Features:**
- Lightweight and fast.
- Extensions for Python, Jupyter Notebooks, and more.
- Integrated Git support.
- Great support for Python debugging and linting

**Installation Instructions:**
- Download VS Code from [the official website.](https://code.visualstudio.com/)
- Run the installer for your operating system and follow the on-screen instructions
- Install Python Extension:
    After launching VS Code, go to the Extensions Marketplace (Ctrl+Shift+X), search for "Python," and install the official Python extension by Microsoft
- Install Python (if not installed already):
    Download Python from [python.org](https://www.python.org/downloads/) and install it on your system.
    Make sure to add Python to your system's PATH during installation

**User Tips:**
- Use VS Code's terminal for executing Python commands.
- Install the Python extension for IntelliSense (auto-completion), linting, and debugging.
- Use Jupyter notebooks inside VS Code by installing the Jupyter extension.

<hr>

## 2. **Jupyter Notebook**
Jupyter Notebook is an open-source web application used for creating and sharing documents that contain live code, equations, visualizations, and narrative text.

**Features :**
- Interactive environment for writing and testing Python code.
- Supports rich media, including images, videos, and LaTeX.
- Great for data science and machine learning projects.

**Installation Instruction**
- Install Jupyter Notebook using pip:

            pip install notebook

- Start Jupyter Notebook:

                jupyter notebook
            
- This will open a new tab in your web browser with the Jupyter

**User Tips :**
- Create new not3ebook by clicking New > Python 3 from Jupyter homepage
- Use Jupyter's <strong>magic commands</strong> like %timeit for performance testing.

<hr>

# 3. **PyCharm**
PyCharm is a powerful, full-featured Integrated Development Environment(IDE) specifically designed for Python development 

**Features :**
- Intelligent code completion.
- Powerful debugging tools.
- Integrated testing support. 
- Built-in support for web frameworks like Django and Flask.

**Installation Instructions :**
- Download Pycharm from the [the official website.](https://www.jetbrains.com/pycharm/download/?section=windows)
- Choose the appropriate version
- Run the installer and follow the instructions to complete the installation.
- After installation, open PyCharm, and you can create a new project or open an existing one.

**User Tips:**
- Use Virtual Environments for each project to avoid dependency conflicts.
- Take advantage of PyCharm's built-in tools like the interactive Python console, integrated terminal, and code inspections.

<hr>

# 4. **Spyder :**

Spyder is a scientific Python IDE specifically designed for Data Science, scientific computing, and machine learning tasks

**Features:**
- Integrated IPython console.
- Advanced variable explorer.
- Supports debugging, profiling, and data visualization.

**Installation Instructions:**

- Install Spyder via Anaconda (recommended for easier setup with all dependencies):

                conda install spyder

Alternatively, you can install Spyder using pip:

            pip install spyder

- Launch Spyder:

    - Open Anaconda Navigator and click Launch under Spyder.
    - Or open a terminal and type:
               
                spyder

**User Tips:**
- Use the Variable Explorer to monitor variables in your current workspace.
- Leverage the IPython console for interactive computing.

<hr>

# 5. **Sublime Text**
Sublime Text is a sophisticated text editor for code, markup, and prose. It’s lightweight and can be enhanced using a variety of packages.
**Features:**
- Extremely fast and responsive.
- Support for Python syntax highlighting and autocompletion.
- Extensive package support via Package Control.

**Installation Instructions:**
- Download Sublime Text from the [official website.](https://www.sublimetext.com/)
- Run the installer and follow the instructions to complete the installation.
- Install the Python package for better Python support:
    - Open Sublime Text, go to Tools > Install Package Control (if it's not already installed).
    - Use Package Control (Ctrl+Shift+P), search for "Python," and install the Python-related packages (e.g., Python PEP8 auto-formatting, linting).

**User Tips:**
- Customize key bindings and snippets for faster coding.
- Use Git integration via the GitGutter package to track changes.
