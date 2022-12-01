class Buses :
   print()
   print("************* Welcome to our Booking application *************")
   print()
   global name
   name = input("Enter your name to view the available buses : ")
def menu():
    print()
    print("-----------------------------------------")
    print()
    print("The Available Buses :")
    print()
    print("1. BusN1  *** From Gaza to Khan Younis ***")
    print("2. BusN2  *** From Rafah to Gaza ***")
    print("3. BusN3  *** From Gaza to  Deir al-Balah ***")
def chooseBus():
    global choice
    choice = int(input("Choose one of these available Buses :"))

def showseats():
    print()
    print("-----------------------------------------")
    print("The Available seats in these bus :")
    print()
    global list
    list=[(1),(2),(3),(4),(5),(6),(7),(8),(9),(10)]
    print(list)

def chooseSeat():
    global seatchoice
    seatchoice = int(input("Choose one of these available Seats :"))

while(True):
    menu()
    quitt=str(input("do you want to quit Y/N ?"))
    if (quitt=="Y"):
        break
    elif (quitt == "N"):
        chooseBus()
    if (choice >3):
        break
    showseats()
    quitt = str(input("do you want to quit Y/N ?"))
    if (quitt == "Y"):
        break
    elif(quitt == "N"):
        chooseSeat()
    print("seat number ",seatchoice,"in bus number ",choice , "has been booked by ", name)
    another=str(input("do you to book another seat (Y/N) ?"))
    if(another=="Y"):
        print("The Available seats in these bus :")
        print()
        global list
        list=[(1),(2),(3),(4),(5),(6),(7),(8),(9),(10)]
        s = seatchoice - 1
        del list[s]
        print(list)
        chooseSeat()
        print("seat number ", seatchoice, "in bus number ", choice, "has been booked by ", name)
    break






