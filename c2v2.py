import subprocess
import time


# Tick Prompts [!] [*] [+]

info = "[*]"
success = "[+]"
failure = "[!]"

# ANSI escape codes for text formatting
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
BLUE = "\033[34m"
GREEN = "\033[32m"
RED = "\033[31m"

# UI Hacker Text
def hacker_print(text, leading_spaces=0):

    text_chars = list(text)
    current, mutated = '', ''

    for i in range(len(text)):

        original = text_chars[i]
        current += original
        mutated += f'\033[1;38;5;82m{text_chars[i].upper()}\033[0m'
        print(f'\r{" " * leading_spaces}{mutated}', end='')
        time.sleep(0.05)
        print(f'\r{" " * leading_spaces}{current}', end='')
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

def meterpreter_listener():
    # Define the command to run
    command = 'msfconsole -q -x "use exploit/multi/handler; set LHOST 0.0.0.0; set LPORT 5757; exploit -j"'

    # Use the subprocess module to run the command
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def nc_listener():
    # Define the command to run
    command = ["nc", "-lvnp", "5757"]

    # Use the subprocess module to run the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

print(banner)
hacker_print(f"{GREEN}{info} Select the listener you want to initiate:")
hacker_print(f'{GREEN}[1] Meterpreter')
hacker_print(f'{GREEN}[2] ThreatCat (Netcat)')

choice = input(f"\n{UNDERLINE}{GREEN}OPSC2{RESET} ▶ ")

if choice == "1":
    print(f"\n{GREEN}Initiating Meterpreter listener...")
    meterpreter_listener()
elif choice == "2":
    print(f"\n{GREEN}Initiating ThreatCat listener...")
    nc_listener()
else:
    hacker_print(f"{GREEN}Invalid choice. Exiting...")



