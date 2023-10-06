# I Won't Let You Down - CTF Challenge Writeup

Challenge: I Won't Let You Down
Points: 50
Category: Miscellaneous

## Objective
The objective of the "I Won't Let You Down" challenge is to uncover the flag by interacting with a network service. Your task is to connect to the service and retrieve the flag.

## Solution
To successfully complete the "I Won't Let You Down" challenge, follow these steps:

1. **Port Scanning with Nmap**: Begin by scanning for open ports on the target server using the `nmap` network scanning tool. This step helps identify which ports are available for connection.

2. **Connecting to the Service**: Once you've identified the open port, connect to it using a web browser or alternative methods such as `netcat` (nc) or a Python script.

   - To connect using `netcat`, you can use a command like:
     ```
     nc 155.138.162.158 8888
     ```
   - Alternatively, you can connect using a Python script, like the one below:

     ```python
     from pwn import *

     url = "155.138.162.158"

     connection = remote(url, 8888)

     print(connection.readall().decode())
     ```

3. By successfully connecting to the service, you will retrieve the flag.

## Flag
The flag for this challenge is in the format: `flag{XXXXXXXXXX}`.

Connect to the network service as described in the solution, and you'll obtain the flag in the "I Won't Let You Down" challenge. Good luck!
