import random as rd
import time as t
def role(sum_score_list):
    for r in range(len(sum_score_list)):
            if sum_score_list[r] == 1:
                sum_score_list[r] = 38
            elif sum_score_list[r] == 4:
                sum_score_list[r] = 14
            elif sum_score_list[r] == 8:
                sum_score_list[r] = 30
            elif sum_score_list[r] == 21:
                sum_score_list[r] = 42
            elif sum_score_list[r] == 29:
                sum_score_list[r] = 76
            elif sum_score_list[r] == 32:
                sum_score_list[r] = 10
            elif sum_score_list[r] == 36:
                sum_score_list[r] = 6
            elif sum_score_list[r] == 48:
                sum_score_list[r] = 26
            elif sum_score_list[r] == 50:
                sum_score_list[r] = 67
            elif sum_score_list[r] == 62:
                sum_score_list[r] = 18
            elif sum_score_list[r] == 71:
                sum_score_list[r] = 92
            elif sum_score_list[r] == 80:
                sum_score_list[r] = 99
            elif sum_score_list[r] == 88:
                sum_score_list[r] = 24
            elif sum_score_list[r] == 95:
                sum_score_list[r] = 56
            elif sum_score_list[r] == 97:
                sum_score_list[r] = 78
            elif sum_score_list[r] == 99:
                sum_score_list[r] = 86
            elif sum_score_list[r] > 100: 
                sum_score_list[r] = sum_score_list[r]-q
            elif sum_score_list[r]==100:
                sum_score_list[r]=100 
                print(":---------> We got our winner <--------:")
                print( "any gussss.....")
                print()
                t.sleep(2)
                print(f"----------- WINNER IS ----------")
                print()
                t.sleep(2)
                print(f": ----------> player {r+1} <----------:")
                final_list=dict(zip(player_ls,sum_score_list))
                print(final_list)
                
                exit(0)
            
def roll(a):
    x=rd.randint(1, 6)
    
    
    score_list[a-1].append(x)
    return x 

Number_player = int(input("Enter the number of players: :)"))

player_ls = []
score_list = []
for i in range(Number_player):
    score_list.append([])
i = 1


while(i <= Number_player):
    player_ls.append(f"player{i}")
    i = i + 1
print(player_ls)

sum_score_list = [0] * Number_player
i = 1
while(i < 300):
    print(f"<----------------Round {i} -------------------> ")
    print("Enter to start")
    input()
    j = 1
    while(j <= Number_player):
        print("______________________________")
        q=roll(j)
        print(f"Roll for player {j}: {q} ")
        
        print(score_list)
        
        sum_score_list[j-1] = sum_score_list[j-1]+q 
        role(sum_score_list)
        
        print("total : ",sum_score_list)
            
        print("______________________________")
        print()
        
        
        j = j + 1
    
    i = i + 1
