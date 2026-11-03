od = int(input("ile zjadłeś kebabów"))
do = int(input("podaj mi ile wyrzygałeś kebabuw"))

if od < do:
    for i in range(od, do):
        print(i)
if od > do:
    for i in range(od, do,-1):
        print(i)