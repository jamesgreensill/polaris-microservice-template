import os
import platform
import subprocess
import sys


def run_command(command):
    """Run a system command."""
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    os_name = platform.system()
    match os_name:
        case "Windows":
            setup_script = r"setup\setup.bat"
        case "Linux" | "Darwin":  # Darwin is the system name for macOS
            setup_script = r"/setup/setup.sh"
        case _:
            print(f"Unsupported OS: {os_name}")
            return

    if not os.path.exists(setup_script):
        print(f"{setup_script} not found in the current directory.")
        return

    print(f"Running {setup_script}...")
    run_command(setup_script)


if __name__ == "__main__":
    main()
