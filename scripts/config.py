import requests as r
import json
import os

if not os.path.exists("./config.json"):
    print("welcome to first time setup ^_<")
    config = {
        "Accounts": [],
        "Items": [],
        "cooldownPerCheck": 1,
        "discordWebhook": "",
    }

    roblosecurity = str(input("Enter Primary ROBLOSECURITY: "))
    try:
        userId = r.get("https://users.roblox.com/v1/users/authenticated",
                    cookies={".ROBLOSECURITY": roblosecurity}).json()["id"]
    except:
        print("ROBLOSECURITY is invalid. Restart the script and try again.")
        exit(0)


    friendlyName = str(input("enter cutie patootie name: "))

    config["Accounts"].append({
        "ROBLOSECURITY": roblosecurity,
        "userId": userId,
        "nickName": friendlyName
    })

    cooldownPerLimited = input("enter cooldown per limited (recommended: 0.75): ")
    config["cooldownPerLimited"] = float(cooldownPerLimited)

    discordWebhook = str(input("enter Discord webhook (leave blank for none): "))
    config["discordWebhook"] = discordWebhook


    jsonObject = json.dumps(config, indent=4)

    with open("./config.json", "w") as f:
        f.write(jsonObject)
        f.close()
    
    print("config file created. restart the script.")
    exit(0)

with open("./config.json", "r") as f:
    print("Loading config...")
    config = json.load(f)
    f.close()

jsonObject = None
print("what would you like to edit? \n"
        "1. edit limited IDs \n"
        "2. edit accounts \n"
        "3. add account \n"
        "4. remove account \n"
        "5. cooldown \n"
        "6. discord webhook \n"
        "7. budget \n"
        "8. exit")

choice = int(input(""))
if choice == 1:
    print("what would you like to do? \n")

    print("1. add limited ID")
    print("2. remove limited ID")
    print("3. clear limited IDs")
    print("4. exit")

    choice = int(input(""))
    if choice == 1:
        limitedId = int(input("Enter limited ID: "))
        config["Items"].append({"id": limitedId})
        jsonObject = json.dumps(config, indent=4)
    elif choice == 2:
        print("what limited ID would you like to remove? \n")
        for i, item in enumerate(config["Items"]):
            print(f"{i + 1}. {item['id']}")
        choice = int(input(""))
        if choice > len(config["Items"]) + 1:
            print("Invalid choice.")
            exit(0)
        config["Items"].pop(choice - 1)
        jsonObject = json.dumps(config, indent=4)
    elif choice == 3:
        config["Items"] = []
        jsonObject = json.dumps(config, indent=4)
    else:
        exit(0)

elif choice == 2:
    print("what account would you like to edit? \n")
    for i, account in enumerate(config["Accounts"]):
        if i == 0:
            print(f"{i + 1}. {account['userId']} {account['nickName']} (Primary)")
        else:
            print(f"{i + 1}. {account['userId']} {account['nickName']}")
    choice = int(input(""))
    
    if choice > len(config["Accounts"]) + 1:
        print("Invalid choice.")
        exit(0)

    print("what would you like to edit? \n")
    print("1. ROBLOSECURITY")
    print("2. Friendly name")
    editChoice = int(input(""))

    if editChoice == 1:
        roblosecurity = str(input("enter ROBLOSECURITY: "))
        try:
            userId = r.get("https://users.roblox.com/v1/users/authenticated",
                        cookies={".ROBLOSECURITY": roblosecurity}).json()["id"]
        except:
            print("ROBLOSECURITY is invalid.")
            exit(0)

        config["Accounts"][choice - 1]["ROBLOSECURITY"] = roblosecurity
    elif editChoice == 3:
        friendlyName = str(input("enter cutie patootie name: "))
        config["Accounts"][choice - 1]["nickName"] = friendlyName

    print("ROBLOSECURITY updated.")
    jsonObject = json.dumps(config, indent=4)
elif choice == 3:
    newRoblosecurity = str(input("Enter ROBLOSECURITY: "))

    try:
        userId = r.get("https://users.roblox.com/v1/users/authenticated",
                    cookies={".ROBLOSECURITY": newRoblosecurity}).json()["id"]
    except:
        print("ROBLOSECURITY is invalid.")
        exit(0)

   
    for i, account in enumerate(config["Accounts"]):
        if account["userId"] == userId:
            print("account already exists.")
            exit(0)


    friendlyName = str(input("enter cutie patootie name: "))
    config["Accounts"].append({
        "ROBLOSECURITY": newRoblosecurity,
        "userId": userId,
        "nickName": friendlyName
    })

    jsonObject = json.dumps(config, indent=4)
elif choice == 4:
    print("what account would you like to remove? \n")
    for i, account in enumerate(config["Accounts"]):
        if i == 0:
            print(f"{i + 1}. {account['userId']} {account['nickName']} (Primary)")
        else:
            print(f"{i + 1}. {account['userId']} {account['nickName']}")
        
    choice = int(input(""))
    if choice > len(config["Accounts"]):
        print("Invalid choice.")
        exit(0)

    config["Accounts"].pop(choice - 1)
    jsonObject = json.dumps(config, indent=4)


elif choice == 5:
    cooldownPerCheck = input("enter cooldown per check: ")
    config["cooldownPerCheck"] = float(cooldownPerCheck)
    jsonObject = json.dumps(config, indent=4)  
elif choice == 6:
    discordWebhook = str(input("enter discord webhook (leave blank for none ): "))
    config["discordWebhook"] = discordWebhook
    jsonObject = json.dumps(config, indent=4)
elif choice == 7:
    budget = int(input("enter budget: "))

    config["budget"] = budget
    jsonObject = json.dumps(config, indent=4)
else:
    exit(0)


if jsonObject:
    with open("./config.json", "w") as f:
        f.write(jsonObject)
        f.close()

    print("config file updated.")
    exit(0)