#!/usr/bin/env python3

import os

# Your command to append
command_to_append = "your-command"

# Get the user's shell from the environment variables
user_shell = os.environ.get("SHELL", "")

# Check if the user's shell is Bash
if "bash" in user_shell:
    with open(os.path.expanduser("~/.bashrc"), "a") as bashrc_file:
        bashrc_file.write(command_to_append + "\n")
# Check if the user's shell is Zsh
elif "zsh" in user_shell:
    with open(os.path.expanduser("~/.zshrc"), "a") as zshrc_file:
        zshrc_file.write(command_to_append + "\n")
# If the user's shell is neither Bash nor Zsh, show an error message
else:
    print("Unknown or unsupported shell. Cannot append to rc file.")

