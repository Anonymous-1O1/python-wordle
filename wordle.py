from colorama import Back,init
from random import randint
init(autoreset=True)
words=(open("words.txt","r").read()).split()
c_answer=words[randint(0,len(words)-1)]
guess=1
while guess<=6:
    attempt=input(f"Guess {guess}: ")
    if attempt==c_answer:
        print(Back.GREEN+attempt)
        print("Congradulations! you got the correct answer!")
        break
    else:
        output=[]
        for i in range(5):
            if attempt[i]==c_answer[i]:
                output.append(Back.GREEN+attempt[i])
            else:
                value=False
                for j in range(5):
                    if j!=i:
                        if attempt[i]==c_answer[j]:
                            value=True
                if value:
                    output.append(Back.YELLOW+attempt[i])
                else:
                    output.append(Back.BLACK+attempt[i])
        print("".join(output))
        if guess==6:
            print(f"Incorrect.The answer was {c_answer}.Better luck next time")
        else:
            print("Incorrect, try again.")
    guess+=1