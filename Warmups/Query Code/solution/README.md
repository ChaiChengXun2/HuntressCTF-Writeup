# CTF Challenge Writeup
**Name:** Query Code
**Points:** 50
**Category:** Warmups

## Objective

The objective of this challenge is to reveal the hidden flag encoded within an image file named ```query_code```.

## Solution

1. **Inspect the File**
   - Start by examining the ```query_code``` file.

2. **File Type Investigation**
   - To determine the file's type, use the ```file``` command on the ```query_code``` file. This will help identify the format of the file.

3. **Identifying the Image Format**
   - Upon using the ```file``` command, you will discover that the ```query_code``` file is, in fact, a PNG (Portable Network Graphics) image file. 
   - I then proceed to check if it is corrupted, this can be done using ```xxd``` or ```hexedit```.
   - Check the file header against a typical PNG file header.
   - I found that it isn't corrupted.

4. **Viewing the Image**
   - As you've confirmed that the file is a PNG image, change its format to PNG and view the image. You can use ```hexedit``` to do this. 

5. **QR Code Discovery**
   - After converting the file format and viewing the image, you'll find a QR code within the image.

6. **Extracting the Flag**
   - There are a couple of ways to extract the flag from the QR code:
     - You can scan the QR code using a QR code reader app or tool. This will reveal the flag encoded within the code.
     - Alternatively, on a Linux terminal, you can use the ```zbarimg``` command to decode the QR code and extract its contents, which is the flag.

7. **Using zbarimg**
   - To extract the flag using ``zbarimg``, open your Linux terminal and run the following command:
     ```
     zbarimg query_code.png
     ```

## Flag
The flag for the Query Code challenge is `flag{XXXXXXXXXX}`. Replace 'XXXXXXXXXX' with the actual flag you obtain from decoding the QR code within the "query_code" image.

Congratulations on completing this Warmups challenge! You've demonstrated your ability to decode and extract information from QR codes within images.
