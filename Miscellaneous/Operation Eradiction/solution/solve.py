import subprocess

files = []

def readFiles():
	with open("files.txt", "r") as file:
		content = file.readlines()

		for line in content:
			file = line[:-1].split(" ")[-1].split("/")[-1]
			directory = "/".join(line[:-1].split(" ")[-1].split("/")[:-1])

			files.append({"Directory": directory, "File": file})

def createFiles():
	for file in files:
		file = file["File"]

		with open(f"allFiles/{file}", "w") as create_file: 
			pass

def rewriteFiles():
	for file in files:
		file_name = file["File"]
		directory = file["Directory"]

		local_path = f"/realpath oft the file/{file_name}"
		server_path = f"{directory}/"

		command = f"rclone copy {local_path} operation:{server_path}"
		output = subprocess.check_output(command, shell=True, text=True)
		print(f"Rewriting {file_name}")

readFiles()
rewriteFiles()