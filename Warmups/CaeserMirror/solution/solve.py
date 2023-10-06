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