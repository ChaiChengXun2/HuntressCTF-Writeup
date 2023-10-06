# CaeserMirror - CTF Challenge Writeup

Challenge: CaeserMirror
Points: 50
Category: Warmups

## Objective
The objective of the CaeserMirror challenge is to decipher a message that has been encrypted using the ROT13 cipher and presented in a unique format. Your task is to unravel the message and find the hidden flag.

## Solution
To successfully complete the CaeserMirror challenge, follow these steps:

1. **Identify ROT13 Encryption**: Recognize that the message has been encrypted using the ROT13 cipher, which involves shifting each letter in the alphabet by 13 positions.

2. **Initial Attempt**: Attempting to decrypt the entire file by pasting it into a ROT13 decoder may not reveal the flag as expected.

3. **Mirrored Phrases**: Pay attention to paragraphs or phrases that appear to be flipped or mirrored, as indicated in the challenge description. You'll notice that not all phrases need to be reversed to find the flag; some can be recognized by specific characters such as "_" and "}".

4. **Left and Right Paragraphs**: The message is split into two columns: the left column appears to be fine as it is, while the right column requires mirroring.

5. **Python Script**: I wrote a python script that decrypts it for me. 

Explanation of the Python Code:
```python
left = []
right = []

alphabet = "abcdefghijklmnopqrstuvwxyz"

def main():
	final_message = []

	for i in range(17):
		string = ""

		string += rot13(left[i]).strip()
		string += " " 
		string += rot13(right[i][::-1]).strip()

		final_message.append(string)

	for line in final_message:
		print(line)

def rot13(string):
	decipher = ""
	for char in string: 
		up = char.isupper()
		char = char.lower()

		if char in alphabet:
			old_index = alphabet.find(char)
			new_index = old_index + 13 - 26

			if up: 
				decipher += alphabet[new_index].upper()
			else:
				decipher += alphabet[new_index]
		else:
			decipher += char
	return decipher

def read():
	with open("caesarmirror.txt", "r") as file: 
		contents = file.readlines()

		for line in contents:

			left.append(line[:-1][:44])
			right.append(line[:-1][47:])

main()
```
### Python Script Overview

This Python script decrypts and formats a message encrypted using ROT13. The message is presented in two columns: the left column remains as is, and the right column is reversed. Here's an overview of the script:

1. **Initialization**:
   - Lists `left` and `right` store content from the left and right message columns.
   - `alphabet` holds the lowercase alphabet for ROT13 decryption.

2. **`main` Function**:
   - Iterates through each line of the message.
   - Decrypts the left part and reverses and decrypts the right part.
   - Combines and appends them to `final_message`.
   - Prints the fully decrypted message.

3. **`rot13` Function**:
   - Decrypts ROT13 for a given string, handling uppercase and lowercase letters.

4. **`read` Function**:
   - Reads lines from "caesarmirror.txt" (not explicitly used).

5. **Execution**:
   - Calls the `main` function to decrypt and format the message.

The script automates the process of uncovering the hidden flag in the CaeserMirror challenge.

## Flag

The flag for this challenge is in the format: `flag{XXXXXXXXXX}`.

With the assistance of the Python script, you can successfully decrypt the message and find the flag in the CaeserMirror challenge. Best of luck!

