# Comprezz - CTF Challenge Writeup

Challenge: Comprezz
Points: 50
Category: Warmups

## Objective
The objective of the "Comprezz" challenge is to decompress a given file and reveal the flag hidden within it.

## Solution
To solve the "Comprezz" challenge, I followed these steps:

1. **Analyzing the File**:
   - I began by examining the provided "comprezz" file. When I used the `file` command on the file, it indicated that the data was compressed.

2. **Recognizing the Compression Format**:
   - I conducted online research to understand the compression format used in the file. I discovered that files with a similar format typically have a `.z` extension.

3. **Decompression**:
   - To decompress the file, I used the `uncompress` command with the filename and the `.z` extension. The command I used was: `uncompress filename.z`.

4. **Viewing the Decompressed Data**:
   - However, it's important to note that the `uncompress` tool often requires the file to have the appropriate extension, even if the file headers are correctly formatted.
   - After decompressing the file, I used the `cat` command to view the decompressed data.

By successfully decompressing the file and examining its content, I uncovered the flag hidden within the decompressed data.

## Flag
The flag for this challenge is in the format: `flag{XXXXXXXXXX}`.

In the "Comprezz" challenge, I identified that the file was compressed and recognized it as a `.z`-formatted file. By using the `uncompress` tool and then viewing the decompressed data using the `cat` command, I extracted the flag concealed within the file.
