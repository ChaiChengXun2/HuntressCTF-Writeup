from pwn import *

url = "155.138.162.158"

connection = remote(url, 8888)

print(connection.readall().decode())