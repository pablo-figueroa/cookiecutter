import subprocess

MESSAGE_COLOR = r"\x1b[34m"
RESET_ALL = r"\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

# Subproceso para instalar las librerias en requirements.txt
# subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

#Con conda
#subprocess.call(['conda', 'env', 'create','--file','environment.yml'])

#subprocess.call(["conda", "create", "-n", "{{cookiecutter.environment_name}}"])

#subprocess.call(["mamba", "env", "update", "-n", "{{cookiecutter.environment_name}}", "-f", "environment.yml"])

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", "Initial commit"])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")