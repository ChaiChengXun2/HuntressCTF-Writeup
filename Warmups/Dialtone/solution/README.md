# Dialtone - CTF Challenge Writeup

Challenge: Dialtone
Points: 50
Category: Warmups

## Objective
The objective of the Dialtone challenge is to decode a series of DTMF (dual tone multi frequency) signals embedded in a WAV file to reveal the hidden flag. Your task is to recognize the DTMF tones, convert them into numbers, and then decode the flag.

## Solution
To successfully complete the Dialtone challenge, follow these steps:

1. **Listen to the WAV File**:
   - Start by examining the provided WAV file. When you listen to it, you'll notice that the audio resembles the sound of clicking an older smartphone, with distinctive tones.

2. **DTMF Tones**:
   - The sounds you're hearing are known as DTMF (dual tone multi frequency) tones, often used in telephony systems. They consist of pairs of distinct frequencies that correspond to different numbers on a phone's keypad.

3. **Online Decoder**:
   - To decipher the DTMF signals, you can use an online decoder. Many online tools are available for this purpose. For example, you can use the following decoder: [DTMF Online Decoder](http://dialabc.com/sound/detect/).

4. **Decode the DTMF Signals**:
   - Run the WAV file through the online DTMF decoder. This process will transform the audio into a series of numbers, effectively converting the DTMF tones into their corresponding digits.

5. **Conversion to Hexadecimal**:
   - After decoding the DTMF signals into numbers, you may notice that the resulting numbers can be further converted into hexadecimal by treating them as big integers.

6. **Flag Decoding**:
   - Convert the hexadecimal numbers into ASCII characters to reveal the flag.

7. By following these steps and carefully decoding the DTMF signals, you will successfully uncover the hidden flag.

## Flag
The flag for this challenge is in the format: `flag{XXXXXXXXXX}`.

In the Dialtone challenge, you'll explore the world of DTMF signals and convert them into numbers to reveal the flag. It's a great introduction to audio forensics and decoding techniques. Good luck!
