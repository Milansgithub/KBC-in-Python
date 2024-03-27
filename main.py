name = input("Enter your Name: ")
ques = ["Q1: What is the capital of India?",
        'Q2: Which planet is known as the "Red Planet"?', 
        "Q3: What is the largest mammal in the world?",
        "Q4: How many continents are there in the world?",
        "Q5: What is the largest ocean on Earth?"
        ]
ans = ["New Delhi", "Mumbai", "Calcutta", "Chandigarh", 
       "Mars", "Earth", "Venus", "Jupiter", 
       "Elephant", "Blue Whale", "Hypo", "Rhyno", 
       "4", "5", "6", "7",
       "Pacific Ocean", "Indian Ocean", "Antartic Ocean",  "Arctic Ocean",
       ]

per = input("Are you Ready for KBC(Y for Yes /N for No ): ")
yes = "Y"
no = "N"

# Q1
if (per == yes):
    print("So,",name,"This is your first question you can directly select option number for answer")   
    print(ques[0])
    print("1.",ans[2])
    print("2.", ans[3])
    print("3.",ans[0])
    print("4.", ans[1])
    ans1 = int(input("Option for 1: "))
elif (per==no):
    print("Thank You, Nice Knowing You",name)


# Q2
t1 = 1
if (ans1 == 3):
    print("Congratulations you won your",t1,"Tokens\n")
    print(ques[1])
    print("1.", ans[4])
    print("2.", ans[5])
    print("3.", ans[6])
    print("4.", ans[7])
    ans2 = int(input("Option for 2: "))  
elif(ans1!=3):
    print("Wrong answer",name, "GAME OVER")


# Q3
t2 = 2
if (ans2 == 1):
    print("Congratulations you won another token and here is your third question\n")
    print("Your Third question is here\n")
    print(ques[2])
    print("1.", ans[8])
    print("2.", ans[9])
    print("3.", ans[10])
    print("4.", ans[11])
    ans3 = int(input("Option for 3: "))
else:
    print("Wrong answer",name, "GAME OVER") 
 

# Q4
t3 = 3
if (ans3 == 2):
    print("Congratulations you won",t3,"Tokens\n")
    print("Your Fourth question is here\n")
    print(ques[3])
    print("1.", ans[12])
    print("2.", ans[13])
    print("3.", ans[14])
    print("4.", ans[15] )
    ans4 = int(input("Option for 4: "))
else:
    print("Wrong answer",name, "GAME OVER")


     
# Q5
t4 = 4
if (ans4 == 4):
    print("Congratulations you won",t4,"Tokens\n")
    print("Your Fifth question is here\n")
    print(ques[4])
    print("1.", ans[16])
    print("2.", ans[17])
    print("3.", ans[18])
    print("4.", ans[19] )
    ans5 = int(input("Option for 5: "))
    t4 = 4
else:
    print("Wrong answer",name, "GAME OVER")
     


t5 = 5
if(ans5 == 4):
     print("Congratulations you won 5 tokens. YOU WON",t5,"Tokens\n")

else:
    print("Wrong answer",name, "GAME OVER")   
# Q6
# if (ans5 == 4):
#     print("Congratulations you won 5 tokens\n")
#     print("Your Sixth question is here\n")
#     print(ques[5])
#     print("1.", ans[20])
#     print("2.", ans[21])
#     print("3.", ans[22])
#     print("4.", ans[23] )
# else:
#     print("Wrong answer",name, "GAME OVER")

# ans6 = int(input("Option: "))

# if(ans6 == 2):
#      print("Congratulations you won another tokens.\n")

# else:
#     print("Wrong answer",name, "GAME OVER")

print("Total tokens you won is ")

if (ans3 == 2 ):
    print(t3)
else:
    print(t2)
