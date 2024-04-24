number = 0
inp = 0
while True:
    inp = input("金額を入力してください(finと入力して入力を終えます)")
    pni = inp.isdecimal()
    if inp == "fin":
        break
    elif pni == True:
        number += int(inp)
    else:
        print("数字で入力してください")
print("合計額は", number, "円です")
