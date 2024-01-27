import subprocess
import platform
import os

class WindowsShell:
    """Represents a shell environment in Windows OS."""

    def __init__(self):
        """Initialize the Windows shell."""
        print("Windows shell initiated.")

    def powershell_command(self, command):
        """
        Execute a command in PowerShell.

        Args:
            command (str): The command to execute in PowerShell.
        """
        subprocess.run(["powershell", "-Command", command], check=True)

    def cmd_command(self, command):
        """
        Execute a command in CMD.

        Args:
            command (str): The command to execute in CMD.
        """
        subprocess.run(["cmd", "/c", command], check=True)

    def wsl_command(self, command):
        """
        Execute a command in WSL (Windows Subsystem for Linux).

        Args:
            command (str): The command to execute in WSL.
        """
        subprocess.run(["wsl", command], check=True)

class LinuxShell:
    """Represents a shell environment in Linux OS."""

    def __init__(self):
        """Initialize the Linux shell."""
        self.default_shell = os.environ.get('SHELL', '/bin/bash')
        print(f"Linux shell initiated with default shell: {self.default_shell}")

    def execute_command(self, command):
        """
        Execute a command in the default Linux shell.

        Args:
            command (str): The command to execute.
        """
        if 'bash' in self.default_shell:
            subprocess.run(["bash", "-c", command], check=True)
        elif 'zsh' in self.default_shell:
            subprocess.run(["zsh", "-c", command], check=True)
        elif 'sh' in self.default_shell:
            subprocess.run(["sh", "-c", command], check=True)
        else:
            print(f"Unsupported shell: {self.default_shell}")

class MacShell:
    """Represents a shell environment in macOS."""

    def __init__(self):
        """Initialize the Mac shell."""
        print("Mac shell initiated.")

    def bash_command(self, command):
        """
        Execute a command in bash (Bourne Again shell).

        Args:
            command (str): The command to execute in bash.
        """
        subprocess.run(["bash", "-c", command], check=True)

    def zsh_command(self, command):
        """
        Execute a command in zsh (Z shell).

        Args:
            command (str): The command to execute in zsh.
        """
        subprocess.run(["zsh", "-c", command], check=True)


def get_shell():
    """
    Detect the operating system and return the corresponding shell object.

    Returns:
        An instance of WindowsShell, LinuxShell, or MacShell based on the OS.

    Raises:
        Exception: If the operating system is unsupported.
    """
    os_name = platform.system().lower()
    if os_name == "windows":
        return WindowsShell()
    elif os_name == "linux":
        return LinuxShell()
    elif os_name == "darwin":  # Darwin is the system name for macOS
        return MacShell()
    else:
        raise Exception("Unsupported operating system")


# Instantiating the appropriate shell based on the OS
shell = get_shell()

# Example command usage (uncomment to use):
if isinstance(shell, WindowsShell):
    shell.powershell_command('Write-Host "Hello from Windows on `hostname`, $USER"')
elif isinstance(shell, LinuxShell):
    shell.execute_command('echo "Hello from Linux on `hostname`, $USER"')
elif isinstance(shell, MacShell):
    shell.zsh_command('echo "Hello from MacOs on `hostname`, $USER"')
