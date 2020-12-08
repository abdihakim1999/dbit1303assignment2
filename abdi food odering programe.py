2# THIS IS A FOOD ORDERING SYSTEM FOR ABDI CHOMA AND MEATY BASE

print( "WELLCOME TO ABDI CHOMA AND MEATY BASE")
Table_no =input("Kidly enter your table number:")

print("Thank you for dining with us,your waiter has been informed of your location"+ Table_no +")

print("Kindly choose from our below supper options")

print( "MAIM MENUS FOR TODAY")

print("1. beef choma + ugali""@KSH 890")
print("2. beef choma + ugali + kachumbari" "@KSH 980")
print("3. beefchoma plain " "@KSH 790")
print("4. kachumbari extra" "@KSH 120")
print("5. ugali extra" "@KSH 100 ")
print("6. kuku choma plain""@KSH 1390")
print("7. kuku choma + Ugali " "@KSH 1490" )
print("8. camel back " "@ KSH 1590")
print("9. plater foe all meat mixes" "@ KSH 1700")
print("10. young goat half plater" "@ KSH 2700")
print("11. young goat full plater" "@KSH 3700")
print("12. camel hump" "@ KSH 1700")

def main_menu():

    print( "1. beef choma + ugali")
    print( " 2. beef choma + ugali + kachumbari")
    print("3. beefchoma plain ")
    print( "4. kachumbari extra")
    print("5. ugali extra")
    print(" 6.kuku choma plain")
    print("7.kuku choma + Ugali ")
    print("8. camel back ")
    print("9.plater foe all meat mixes")
    print (" 10. young goat half plater")
    print(" 11. young goat full plater")
    print ("12. camel hump")

order=int(input("Enter choice:"))
if order ==1:
       print( "your beef choma + ugali will be served shortly.Thank you" )
elif order ==2:
    print("your beef choma + ugali + kachumbari will be served shortly.Thank you" )
elif order ==3:
    print("your beefchoma plain will be serverd shortly.Thank YOU")
elif order ==4:
    print("your kachumbari extra will be added shortly.Thank you")
elif order == 5:
    print(" your ugali extra will be added shortly.Thank you")
elif order ==6:
    print("order for kuku choma plain will be serverd shortly.Thank YOU")
elif order ==7:
    print("Your order of kuku choma + Ugali will be serverd shortly.Thank YOU")
elif order ==8:
    print("the delicious camel back will be serverd shortly.Thank YOU")
elif order ==9:
    print(" the plentifull plater foe all meat mixes will be serverd shortly.Thank YOU")
elif order ==10:
    print("the soft young goat half plater will be serverd shortly.Thank YOU")
elif order ==11:
    print (" the amazing camel hump will be serverd shortly.Thank YOU")
else:
    print( "incorrect choice: please use digit 1-12")
    main_menu()