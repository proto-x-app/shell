import subprocess
import platform
import sys
import shutil

def is_choco_installed():
    """Check if Chocolatey is installed on Windows."""
    return shutil.which("choco") is not None

def install_choco():
    """Install Chocolatey on Windows."""
    print("Installing Chocolatey...")
    subprocess.run(["powershell", "Set-ExecutionPolicy", "Bypass", "-Scope", "Process", "-Force"], check=True)
    subprocess.run(["powershell", "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"], check=True)

def is_package_installed(package_name):
    """Check if a package is installed on Ubuntu."""
    try:
        subprocess.run(["dpkg", "-l", package_name], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def docker_installed():
    """Check if Docker is installed."""
    try:
        subprocess.run(["docker", "-v"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def bitwarden_installed():
    """Check if Bitwarden CLI is installed."""
    return shutil.which("bw") is not None

def install_docker_windows():
    """Install Docker using Chocolatey on Windows."""
    print("Installing Docker on Windows...")
    subprocess.run(["choco", "install", "docker-desktop", "-y"], check=True)

def install_bitwarden_windows():
    """Install Bitwarden CLI using Chocolatey on Windows."""
    print("Installing Bitwarden CLI on Windows...")
    subprocess.run(["choco", "install", "bitwarden", "-y"], check=True)

def install_docker_ubuntu():
    """Install Docker on Ubuntu."""
    print("Installing Docker on Ubuntu...")
    # Ubuntu-specific Docker installation commands

def install_bitwarden_ubuntu():
    """Install Bitwarden CLI on Ubuntu."""
    print("Installing Bitwarden CLI on Ubuntu...")
    # Ubuntu-specific Bitwarden CLI installation commands

def ensure_software_installed():
    os_name = platform.system().lower()

    if os_name == "windows":
        if not is_choco_installed():
            install_choco()

        if not docker_installed():
            install_docker_windows()
        else:
            print("Docker is already installed on Windows.")

        if not bitwarden_installed():
            install_bitwarden_windows()
        else:
            print("Bitwarden CLI is already installed on Windows.")

    elif os_name == "linux":
        if not is_package_installed("docker-ce"):
            install_docker_ubuntu()
        else:
            print("Docker is already installed on Ubuntu.")

        if not bitwarden_installed():
            install_bitwarden_ubuntu()
        else:
            print("Bitwarden CLI is already installed on Ubuntu.")

    else:
        print("Unsupported operating system.")
        sys.exit(1)

if __name__ == "__main__":
    ensure_software_installed()
