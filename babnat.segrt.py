from random import randint


Fam_Chosen = []
Fam_List = ["Letizia", "Luigi", "Luca", "Laura", "Lorenzo", "Leonardo"]
Count = 0


while Count < 6:

    member = 7
    while member > 6:
        member = int(input("chi sei? \n\n 1.Letizia\n 2.Luigi\n 3.Luca\n 4.Laura\n 5.Lorenzo\n 6.Leonardo\n"))

    present = randint(1, 6)

    check = Fam_List[present -1] in Fam_Chosen
    while present == member or check == True:
        present = randint(1, 6)
        check = Fam_List[present -1] in Fam_Chosen
        
    #print(check, Fam_List[present - 1], Fam_Choose)

    if present != member and check == False and member <= 6:
        print(Fam_List[member - 1], "il ricevente del tuo regalo e' stato scelto\n")
        Fam_Chosen.append(Fam_List[present - 1]) 
        member_file = Fam_List[member - 1] + ".txt"
        doc = open(member_file, "w")
        doc.write(Fam_List[present - 1])
        doc.close()
        Count += 1

if Count >= 6:
    print("abbiamo finito")

    

        
            
            


        
