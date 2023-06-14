A Python virtual environment is a tool that allows you to create isolated and self-contained Python environments. It helps manage dependencies and prevents conflicts between different Python projects. Here are a few examples of working with Python virtual environments:

1. Creating a virtual environment:
   ```bash
   python -m venv myenv
   ```
   This command creates a new virtual environment named `myenv` in the current directory.

2. Activating a virtual environment:
   ```bash
   source myenv/bin/activate
   ```
   This command activates the virtual environment `myenv`. You will notice that the command prompt changes, indicating that you are now working within the virtual environment.

3. Installing packages within a virtual environment:
   ```bash
   pip install package_name
   ```
   This command installs a Python package (`package_name`) within the active virtual environment.

4. Listing installed packages within a virtual environment:
   ```bash
   pip list
   ```
   This command lists all the installed packages within the active virtual environment.

5. Deactivating a virtual environment:
   ```bash
   deactivate
   ```
   This command deactivates the active virtual environment and returns you to the original system Python environment.

Python virtual environments are particularly useful when working on multiple projects with different dependencies. Each project can have its own isolated environment, allowing you to manage and update dependencies independently.

Remember to adjust the above commands based on your operating system. The examples provided assume a Unix-like shell environment. For Windows, the commands may differ slightly.

By utilizing Python virtual environments, you can maintain clean and separate environments for each project, ensuring consistent and reproducible development environments.