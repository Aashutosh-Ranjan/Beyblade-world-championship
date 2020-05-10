from decimal import  Decimal
def beyblade():
    while(True):
        no_players=input("Enter an integer for the no of players for the fight in the range of 1 to 1e5 => ")
        try:
            no_players=Decimal(no_players)
            if(no_players!=int(no_players) or no_players < 1  or  no_players > 1e5):
                continue
            break
        except:
            continue
        
        
    no_players=int(no_players)    
    while(True):
        team_G = input(f"Enter integers for the strength of {no_players} members of your team_G in the range of 1 to 1e5 in space separated format ")
        team_G = team_G.split()
        if(len(team_G)!=no_players):
            continue
        each_g_list=[]
        for i in range(no_players):
            
            try:
                each_g=Decimal(team_G[i])
                if(each_g!=int(each_g) or each_g < 0  or  each_g > 1e5):
                    break
                each_g_list.append(int(each_g))
            except:
                break
        if len(each_g_list)!=no_players:
            continue
        else:
            break
        
    while(True):
        team_o = input(f"Enter integers for the strength of {no_players} members of opponent team in the range of 1 to 1e5 in space separated format ")
        team_o = team_o.split()
        if(len(team_o)!=no_players):
            print('a')
            continue
        each_o_list=[]
        for i in range(no_players):
            
            try:
                each_o=Decimal(team_o[i])
                if(each_o!=int(each_o) or each_o < 0  or  each_o > 1e5):
                    break
                each_o_list.append(int(each_o))
            except:
                break
        if len(each_o_list)!=no_players:
            print('b',each_o_list,no_players,team_o)
            continue
        else:
            break
    each_g_list.sort()
    each_o_list.sort()
    wins=0
    for i in each_o_list:
        flag=0
        for j in each_g_list:
            if(j>i):
                wins+=1
                flag=1
                each_g_list.remove(j)
                break
        if flag==0:
            mini=min(each_g_list)
            each_g_list.remove(min(each_g_list))
    print(f'The maximum wins from the most optimal order is {wins}')
    return wins
            
        
beyblade()      
            