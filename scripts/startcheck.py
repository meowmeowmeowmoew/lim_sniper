import os

if not os.path.exists("./config.json"):
    print("ensuring pip is installed")
    os.system("python -m ensurepip --upgrade")

    print("installing required packages")
    os.system("python -m pip install -r ./requirements.txt")
    exit(0)