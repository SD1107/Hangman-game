import random
print("\t\t\t\t\t _                                             ")                                               
print("\t\t\t\t\t| |                                            ")
print("\t\t\t\t\t| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
print("\t\t\t\t\t| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ ")
print("\t\t\t\t\t| | | | (_| | | | | (_| | | | | | | (_| | | | |")
print("\t\t\t\t\t|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| ")
print(" \t\t\t\t\t                   __/ |                       ")
print("\t\t\t\t\t                   |___/                        ")
#print("      ***************HANGMAN GAME***************")
print("\t\t\tIn this game you have to Predict the word based on the given number of dashes.")
print("\t\t\tYou only have 6 lives to guess the word exhausting which you will lose the game.")
print("\t\t\tFor every incorrect guess you will lose one life. So use your chances well!")
print("\t\t\tAll the best !")
words=["complex",
"puzzle",
"difficult",
"challenge",
"problem",
"mystery",
"enigma",
"conundrum",
"dilemma",
"quandary",
"nostalgia",
"fortuitous",
"whimsical",
"melancholy",
"resilient",
"ethereal",
"serene",
"vivacious",
"gregarious",
"introspective"]
number=random.randint(0,len(words)-1)
aim=words[number]
chances=6
#print(aim)
length=len(aim)
str=""
for i in range(1,length+1):
    str=str+"_"
#print(str)
flag=0
count=0
while chances>0:
    flag=0
    print(f"Word to guess: {str}")
    letter=input("Guess a letter: ")
    for i in range(0,len(aim)):
        if letter==aim[i]:
            str=str[:i]+letter+str[i+1:]
            flag=1
    if(flag==1):
        print(str)
    elif(flag==0):
        chances=chances-1
    print("           ***********************")
    print(f"Lives left = {chances}")
    if str==aim:
        count=1
        break
if count==1:
    print("Congratulations! You have correctly guessed the word!")
    print(f"The correct wor was :{aim}!")
    print("          ***********THE END**********")
else:
    print("Sorry you have run out of lives! Better luck next time!")
    print(f"The correct wor was :{aim}!")
    print("          ***********THE END**********")
    
