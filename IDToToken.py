import base64
import os
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init()

# Resize Command Prompt window (Windows only)
os.system("mode con: cols=125 lines=35")  # Adjusts width and height

# Cool title banner in BLUE with centered links
title = Fore.BLUE + Style.BRIGHT + """
██╗██████╗░  ████████╗░█████╗░  ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗
██║██╔══██╗  ╚══██╔══╝██╔══██╗  ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║
██║██║░░██║  ░░░██║░░░██║░░██║  ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║         Website: https://kegean.github.io/
██║██║░░██║  ░░░██║░░░██║░░██║  ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║         Discord: https://discord.gg/m9mV7W9KnY
██║██████╔╝  ░░░██║░░░╚█████╔╝  ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║         GitHub:  https://github.com/Kegean
╚═╝╚═════╝░  ░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝
""" + Style.RESET_ALL

print(title)

# Prompt user for their Discord ID in RED
discord_id = input(Fore.RED + Style.BRIGHT + "\nEnter your Discord ID: " + Style.RESET_ALL)

# Encode the ID using Base64
encoded_id = base64.b64encode(discord_id.encode()).decode()
print(Fore.RED + Style.BRIGHT + f"\nEncoded ID (Base64): {encoded_id}" + Style.RESET_ALL)

# Display the first half of the encoded string in RED
half_length = len(encoded_id) // 2
print(Fore.RED + Style.BRIGHT + f"\nFirst half: {encoded_id[:half_length]}" + Style.RESET_ALL)
input("\nPress Enter to exit...")
