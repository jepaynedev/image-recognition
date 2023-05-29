# Setup

This project will be run on Window and use Python 3.8. I will attempt to keep code cross-platform where I have a choice and am aware of difference, but I do not plan on testing on other systems. I will try to note where I expect potential difference, but any required adjustments to the instructures will be the responsibilty of the user.

## Install Python

### Windows

- [Download Python](https://www.python.org/downloads/). This project requires 3.8+. If you only have an older version on your system (or are unsure), installing the latest version should be sufficient.

- _(Recommended)_ Create a virtual environment:

  Open a terminal and in your working directory run:

  `py -m venv .venv`

  This will user the Windows Python launcher to invoke specifically the installed 3.8 version of Python. The `-m venv` option invokes the standard library venv module, and the final `.venv` is the name of the virtual environment folder to be created.

  Depending on terminal used, run the appropriate command to activate the virtual environment

  - PowerShell: `.\venv\Scripts\Activate.ps1`
  - cmd.exe: `venv\Scripts\activate.bat`

  At any point after, running `deativate` will deactivate the virtual environment

  I will usually run `python -m pip install --upgrade pip` upon initial creation or occasionally if prompted with a warning to ensure that the [Pip package manager](https://pypi.org/project/pip/) used for installing dependencies is updated.

### Linux/Mac

Installation instructions and optional virtual environment setup may vary based on system or distribution.
