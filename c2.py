import subprocess

# ANSI escape codes for text formatting
BOLD = "\033[1m"
RESET = "\033[0m"
BLUE = "\033[34m"
GREEN = "\033[32m"

# Define your ASCII art banner
banner = r"""

 ██████╗ ██████╗ ███████╗     ██████╗██████╗
██╔═══██╗██╔══██╗██╔════╝    ██╔════╝╚════██╗
██║   ██║██████╔╝███████╗    ██║      █████╔╝
██║   ██║██╔═══╝ ╚════██║    ██║     ██╔═══╝
╚██████╔╝██║     ███████║    ╚██████╗███████╗
 ╚═════╝ ╚═╝     ╚══════╝     ╚═════╝╚══════╝
                                        v1.0
"""
def nc_listener():
   # Define the command to run
   command = ["nc", "-lvnp", "5757"]

   # Use the subprocess module to run the command
   try:
       subprocess.run(command, check=True)
   except subprocess.CalledProcessError as e:
       print(f"Error: {e}")


print(banner)
print("Listening")
nc_listener()

