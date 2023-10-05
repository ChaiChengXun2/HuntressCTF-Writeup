# CTF Challenge Writeup
**Name:** BaseFFFF+1
**Points:** 50
**Category:** Warmups

## Objective

The objective of this challenge is to decode and extract a hidden flag from the provided file, ```baseffff1``` To do this, you'll need to identify the encoding used and create a script to decode it.

## Solution

1. **Analyzing the File**
   - Begin by examining the contents of the ```baseffff1``` file. You'll notice that it contains a mix of Chinese characters and unprintable characters.

2. **Decoding Challenge**
   - The characters that appear as unprintable are actually the result of the ```cat``` command trying to interpret and display the file content.
   - Initially, it might seem like a character set shifting challenge, but that's not the case.

3. **Cracking the Title Clue**
   - Take a closer look at the title of the challenge, which mentions ```FFFF+1```. 
   - Convert the hexadecimal value ```FFFF``` to its decimal representation. ```FFFF``` in hexadecimal is equal to ```65535```.
   - Now, add ```1``` to ```65535```, and you get ```65536```.

4. **Discovering Base65536 Encoding**
   - To solve the challenge, search for ```base65536``` encoding online. You will find that it's a specific encoding scheme that allows large numbers to be represented in a compact way using Unicode characters.

5. **Using Python to Decode**
   - To decode the content, you can utilize a Python library for ```base65536```. Start by installing the library using ```pip```:
     ```
     pip install base65536
     ```
   - After installation, you can create a Python script to do the decoding work.

6. **Python Script**
   - Below is a Python script that decodes the content from the ```baseffff1``` file:
     ```python
     import base65536

     with open("baseffff1", "r") as file:
         content = file.readlines()
         flag = base65536.decode(content[0]).decode().replace("Nice work! We might have played with too many bases here... 0xFFFF is 65535, 65535+1 is 65536! Well anyway, here is your flag:\r\n\r\n", "")
         print(flag)
     ```

7. **Flag Extraction**
   - Upon running the script, the decoded flag will be revealed. This flag is what you need to complete the challenge.

## Flag
The flag for the BaseFFFF+1 challenge is `flag{XXXXXXXXXX}`. Replace 'XXXXXXXXXX' with the actual flag obtained by decoding the content from the "baseffff1" file.

Congratulations on completing this Warmups challenge! You've demonstrated your ability to identify encoding schemes and create scripts for decoding.
