# inicializar un reporte de git
# verificar que un valor tenga el contenido adecuado

#print('Hello')

import os
import sys

PROJECT_SLUG = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = r"\x1b[31m" # To change the terminal color
MESSAGE_COLOR = r"\x1b[34m"
RESET_ALL = r"\x1b[0m"

if PROJECT_SLUG.startswith("x"):
    print(f"{ERROR_COLOR}ERROR: {PROJECT_SLUG=} is not a valid name for this template.{RESET_ALL}")

    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome!")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")