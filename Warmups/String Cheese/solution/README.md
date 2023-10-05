# CTF Challenge Writeup
**Name:** String Cheese
**Points:** 50
**Category:** Warmups

## Objective

The objective of this challenge is to extract a flag from the given image file, ```cheese.jpg``` To accomplish this, you need to employ basic forensic tools.

## Solution

1. **Downloading the Image**
   - Start by downloading the provided image file, ```cheese.jpg``` This file is your starting point for the challenge.

2. **Using Exiftool (Attempt 1)**
   - Initially, you can try using `exiftool` to inspect the image and look for potential metadata that might contain the flag. Exiftool is commonly used for extracting metadata from files.

3. **Alternative Approach with Strings (Attempt 2)**
   - If the first attempt with `exiftool` doesn't yield the flag, don't worry. You can employ the `strings` command to analyze the contents of the image.

4. **Searching for the Flag**
   - To find the flag, use the following command:
     ```
     strings cheese.jpg | grep -i "flag"
     ```
   - This command extracts all the strings from the image and searches for the keyword "flag" in a case-insensitive manner.

5. **Flag Discovery**
   - Upon executing the command, you will discover the flag that matches the specified format. This flag is what you need to complete the challenge.

## Flag
The flag for the String Cheese challenge is `flag{XXXXXXXXXX}`. Replace 'XXXXXXXXXX' with the actual flag you obtain after successfully extracting it from the image using the provided commands.

Congratulations on completing this Warmups challenge! You've practiced using basic forensic tools like `strings` to uncover hidden information within images.
