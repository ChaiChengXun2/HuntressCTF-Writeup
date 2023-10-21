flag = ""

with open("purview.csv", "r") as file:
	content = file.readlines() 

	for line in content:
		if "new-inboxrule" in line.lower():
			flag += line.split(",")[18][-3]

print(flag)