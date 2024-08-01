import random
p1=0
p2=0
while ((p1<25) or (p2<25)):
    for i in range(1):
        print("[*************PLAYER 1:*************]")
        ask=int(input("Enter 1 if you want to roll the dice else 0: "))
        if(ask==1):
            x=random.randint(1,4)
            print(f"Initial position :  {p1}")
            print(f"dice roll :  {x}")
            p1=p1+x
            print(f"new position :  {p1}")
            if p1==24:
                p1=2
                print("Snake bite!!!!!🐍 🐍")
            elif p1==19:
                p1=7
                print("Snake bite!!!!!🐍 🐍")
            elif p1==17:
                p1=9
                print("Snake bite!!!!!🐍 🐍")
            elif p1==5:
                p1=11
                print("Climbing ladder :)...🪜 🪜")
            elif p1==8:
                p1==18
                print("Climbing ladder :)...🪜 🪜")
            elif p1>25:
                p1=p1-x
            elif p1==25:
                print("         I won🤌            ")
        elif(ask==0):
            print("🥲 🥲 🥲 🥲 🥲 end game 🥲 🥲 🥲 🥲 🥲")
            break
        else:
            print("❌ ❌ ❌ ❌ ❌ invalid ❌ ❌ ❌ ❌ ❌")
            continue
        print("---------------------position of players after 1st player played------------------")  
        print(f"[player1: {p1}]------------[player2: {p2}]")
        if p1==p2:
            p2=0
            print("Go to start🫡🫡 Player2")        
        print("*************PLAYER 2:*************")
        ask=int(input("Enter 1 if you want to roll the dice else 0: "))
        if(ask==1):
            x=random.randint(1,4)
            print(f"initial position: {p2}")
            print(f"dice roll =  {x}")
            p2=p2+x
            print(f"new position:  {p2}")
            if p2==24:
                p2=2
                print("Snake bite!!!!!🐍 🐍")
            elif p2==19:
                p2=7
                print("Snake bite!!!!!🐍 🐍")
            elif p2==17:
                p2=9
                print("Snake bite!!!!!🐍 🐍")
            elif p2==5:
                p2=11
                print("Climbing ladder :)...🪜 🪜")
            elif p2==8:
                p2==18
                print("Climbing ladder :)...🪜 🪜")
            elif p2>25:
                p2=p2-x
            elif p2==25:
                print("          I won🤌            ")
        elif(ask==0):
            print("🥲 🥲 🥲 🥲 🥲 end game 🥲 🥲 🥲 🥲 🥲")
            break
        else:
            print("❌ ❌ ❌ ❌ ❌ invalid ❌ ❌ ❌ ❌ ❌")
            continue
        print("--------------------position of players after 2nd player played------------------")
        print("###################################################################################")
        print(f"[player1:{p1}]------------[player2:{p2}]")
        if p2==p1:
            p1=0
            print("Go to start🫡 🫡 Player1")