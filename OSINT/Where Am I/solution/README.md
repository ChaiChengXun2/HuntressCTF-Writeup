# Where Am I? - CTF Challenge Writeup

Challenge: Where Am I?  
Points: 50  
Category: OSINT  

## Objective
The objective of the "Where Am I?" challenge is to identify the location depicted in an image and extract the flag hidden within it.

## Solution
To solve the "Where Am I?" challenge, I followed these steps:

1. **Analyzing the Image**:
   - I began by examining the image provided in the challenge. The image seemed to contain location-related information.

2. **Extracting Metadata**:
   - I used the `exiftool` utility to extract metadata from the image. Exif data often contains useful information about the image.

3. **Identifying the Hidden Message**:
   - While I initially thought this challenge might involve geolocation OSINT (Open Source Intelligence), I discovered something interesting in the extracted exif data.
   - The exif data contained a base64-encoded message.

4. **Decoding the Flag**:
   - I decoded the base64 message to reveal the flag hidden within the image.

By examining the image's exif data and decoding the base64 message, I successfully uncovered the flag hidden within the image.

## Flag
The flag for this challenge is in the format: `flag{XXXXXXXXXX}`.

In the "Where Am I?" challenge, I analyzed the image's exif data to discover a base64-encoded message. After decoding this message, I obtained the flag concealed within the image.
