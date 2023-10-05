import base65536

with open("baseffff1", "r") as file:
    content = file.readlines()
    flag = base65536.decode(content[0]).decode().replace("Nice work! We might have played with too many bases here... 0xFFFF is 65535, 65535+1 is 65536! Well anyway, here is your flag:\r\n\r\n", "")
    print(flag)