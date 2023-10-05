# CTF Challenge Writeup
**Name:** Notepad
**Points:** 50
**Category:** Warmups

## Objective

The objective of this challenge is simple: download the provided ```notepad``` file and extract the flag hidden within it. You'll be using basic command-line tools to achieve this.

## Solution

1. **Downloading the File**
   - Start by downloading the ```notepad``` file provided as part of the challenge. This file is your entry point to the challenge.

2. **Using 'cat' (Alternative: 'strings')**
   - To extract the flag, you can use the ```cat``` command, a standard utility for displaying the contents of a file in the terminal.
   - Simply run the following command:
     ```
     cat notepad
     ```
   - This will print out the contents of the ```notepad``` file, including the flag.

   Alternative Approach:
   - Instead of using 'cat,' you can also employ the ```strings``` command, which extracts printable strings from the file. This can help you identify the flag within the file.

## Flag
The flag for the Notepad challenge is `flag{XXXXXXXXXX}`. Replace 'XXXXXXXXXX' with the actual flag you obtain after running the provided command to extract it from the "notepad" file.

Congratulations on completing this Warmups challenge! You've practiced using basic command-line tools to uncover hidden information within files.
