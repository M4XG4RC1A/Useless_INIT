print("welcome to contradiction machine\n")
cond = True
resOk = "Yes"
TradNo = {"YES":"Yes","NO":"No"}
TradYes = {"YES":"No","NO":"Yes"}
while cond:
    res = input(resOk+"? ")
    if res.upper() == "YES":
        resOk = TradYes[resOk.upper()]
    if res.upper() == "NO":
        resOk = TradNo[resOk.upper()]
    if res.upper() == "PLEASE END, I CAN'T DO THIS MORE TIME":
        print("You Lose :)\n")
        cond = False
