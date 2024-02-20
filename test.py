import os, subprocess
from dotenv import load_dotenv
from io import StringIO

decrypted = subprocess.run(['sops', '-d', '.env'], capture_output=True, text=True)

conf=StringIO(decrypted.stdout)
load_dotenv(stream=conf)
print(os.environ.get("secret"))

