import subprocess
import time

# ANSI escape codes for text formatting
BOLD = "\033[1m"
RESET = "\033[0m"
BLUE = "\033[34m"
GREEN = "\033[32m"

# UI Hacker Text
def hacker_print(text, leading_spaces = 0):

	text_chars = list(text)
	current, mutated = '', ''

	for i in range(len(text)):
		
		original = text_chars[i]
		current += original
		mutated += f'\033[1;38;5;82m{text_chars[i].upper()}\033[0m'
		print(f'\r{" " * leading_spaces}{mutated}', end = '')
		time.sleep(0.05)
		print(f'\r{" " * leading_spaces}{current}', end = '')
		mutated = current

	print(f'\r{" " * leading_spaces}{text}\n')


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
hacker_print(f"{GREEN}Initiating listener..")
nc_listener()

