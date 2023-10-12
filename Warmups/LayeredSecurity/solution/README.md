# LayeredSecurity - CTF Challenge Writeup

Challenge: LayeredSecurity  
Points: 50  
Category: Warmups  

## Objective
The objective of the "LayeredSecurity" challenge is to uncover the hidden flag within a GIMP image that has been concealed under multiple layers of security.

## Solution
To solve the "LayeredSecurity" challenge, I followed these steps:

1. **File Analysis**:
   - I began by examining the downloaded file using the `file` command. It revealed that the file was a GIMP image.

2. **Opening the Image**:
   - I used the GIMP image editor to open the image. GIMP is a popular open-source image manipulation software.

3. **Layer Removal**:
   - Inside GIMP, I noticed that the image was comprised of multiple layers, which indicated the "layered security" aspect of the challenge.
   - I began the process of slowly removing the layers on the image, one by one.

4. **Flag Discovery**:
   - After removing the layers, I uncovered the unencrypted flag that was hidden beneath them.

By carefully analyzing the layers of the GIMP image and systematically removing them, I successfully revealed the flag hidden within the image.

## Flag
The flag for this challenge is in the format: `flag{XXXXXXXXXX}`.

In the "LayeredSecurity" challenge, I used the GIMP image editor to open an image containing multiple layers of security. By removing these layers, I uncovered the hidden flag within the image.
