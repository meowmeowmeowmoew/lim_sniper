import httpx as r

print("checking for updates...")
script = r.get("https://github.com/meowmeowmeowmoew/lim-sniper/blob/main/main.py").text
with open("main.py", "r") as f:
   if f.read() != script:
        print("updating...")
        with open("main.py", "w") as f:
            f.write(script)
            exit(0)
