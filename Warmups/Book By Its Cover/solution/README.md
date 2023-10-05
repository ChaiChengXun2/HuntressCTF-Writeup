# CTF Challenge Writeup
**Name:** Book By Its Cover
**Points:** 50
**Category:** Warmups

## Objective

The objective of this challenge is to explore a file that seems to be a RAR archive but isn't what it appears to be. By investigating the file's true format and manipulating it, you'll discover the hidden flag.

## Solution

1. **Downloading and Extracting the File**
   - Begin by downloading the ```book.rar``` RAR file provided for the challenge. This file serves as the starting point.

2. **Unrar Attempt**
   - Initially, you might try extracting the file using the ```unrar``` command, as it's named as a RAR archive: 
     ```
     unrar e book.rar
     ```
   - However, you may find that the file extraction fails, indicating that it isn't a valid RAR archive.

3. **Determining the File Type**
   - To unravel the mystery, you should identify the actual file type. Use the ```file``` command to examine the file:
     ```
     file book.rar
     ```
   - This command will reveal the true format of the file.

4. **Discovering the True Format**
   - You will find that the file is not a RAR archive as expected. Instead, it's identified as a PNG image.

5. **Modifying the File Header**
   - Armed with this knowledge, you need to manipulate the file to transform it into a viewable image. To do this, use a hex editor tool, such as ```hexedit```, to modify the file's header.
   - Open the file with the hex editor, navigate to the file header section, and make the necessary changes to reflect the PNG format.

6. **Viewing the Image**
   - After modifying the file's header, save the changes and exit the hex editor. Now, you can view the image as a PNG file.

7. **Flag Discovery**
   - Within the image, you will discover the flag hidden in the usual format. This flag is what you need to complete the challenge.

## Flag
The flag for the Book By Its Cover challenge is `flag{XXXXXXXXXX}`. Replace 'XXXXXXXXXX' with the actual flag you uncover from the manipulated image file.

Congratulations on completing this Warmups challenge! You've practiced identifying file formats and using hex editors to reveal hidden information.
