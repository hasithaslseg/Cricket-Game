import random
from colorama import Fore
n=1
class batsman:
    def __init__(self,name,nick,hand,score,balls_faced,status):
        self.name=name
        self.nick=nick
        self.hand=hand
        self.score=score
        self.balls_faced=balls_faced
        self.status=status

    def bat(self):
        list1=[1,1,1,1,2,1,1,1,1,1,2,2,2,2,3,4,6,0]
        n = random.choice(list1)
        self.score=self.score+n
        self.balls_faced=self.balls_faced+1
        #print(f"You got {n} runs")
        return n



class bowler:
    def __int__(self,name,hand,wickets,balls_bowled):
        self.name=name
        self.hand=hand
        self.wickets=wickets
        self.balls_bowled=balls_bowled


sanath=batsman ("Sanath Jayasooriya","sanath","left",0,0,"Not Out")
kalu=batsman ("Romesh Kaluwitharana","kalu","right",0,0,"Not Out")
gura=batsman ("Asanka Gurusinghe","gura","left",0,0,"Not Out")
ara=batsman ("Aravinda de Silva","ara","right",0,0,"Not Out")
hashan=batsman ("Hashan Thilakarathne","hashan","left",0,0,"Not Out")
vass=batsman ("Chaminda Vass","vass","left",0,0,"Not Out")

pool_of_players=[sanath,kalu,gura,ara,hashan,vass]


def add_player():
    pool_of_players2=[]
    name= input("Please Enter Name of the Player :")
    nick_name=input("Please Enter Nick Name of the Player: ")
    nick_name2=nick_name
    hand=input("Left hand or Right hand: ")

    for yy in pool_of_players:
        pool_of_players2.append(yy.nick)
    if nick_name not in pool_of_players2:
        globals()[nick_name] = batsman(name,nick_name2,hand,0,0,"Not Out")
        pool_of_players.append(globals()[nick_name])
    else:
        print("The Player Already in the Pool")



i=0
no_of_batters=6
list_nick=[]

def bat_order():
    bat_order = []
    list_nick = []
    for za in pool_of_players:
        list_nick.append(za.nick)
    print(Fore.WHITE,f"the available players are\n  {list_nick}")
    for batting_position in range (0,no_of_batters):

        batter_name=input(f"Enter the name of Batting Position {batting_position+1} :")

        while batter_name not in list_nick:
            print("Your player is not in the pool or already allocated")
            print(f"the available players are\n  {list_nick}")
            batter_name = input(f"Enter the name of Batting Position {batting_position + 1} :")
        for z in pool_of_players:
            if z.nick==batter_name:
                bat_order.append(z)
                pool_of_players.remove(z)
        list_nick=[]
        for za in pool_of_players:
            list_nick.append(za.nick)
        print(f"The available players are {list_nick}")





    return bat_order

def playmatch (no_of_balls,bat_order):
    i=0
    for x in range(0, no_of_balls):
        score=bat_order[i].bat()
        if score==0:
            bat_order[i].status="Out"
            i=i+1
        if i==len(bat_order):
            print ("-----------------------ALL OUT-------------------")
            print(f"No of balls faced {x+1}")
            break

tot=0
def print_scorecard():
    print("--------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------")
    print(Fore.GREEN, f"{batt_order[0].name}              {batt_order[0].score}     ({batt_order[0].balls_faced})   {batt_order[0].status}")
    print(Fore.GREEN, f"{batt_order[1].name}              {batt_order[1].score}     ({batt_order[1].balls_faced})   {batt_order[1].status}")
    print(Fore.GREEN, f"{batt_order[2].name}              {batt_order[2].score}     ({batt_order[2].balls_faced})  {batt_order[2].status}")
    print(Fore.GREEN, f"{batt_order[3].name}              {batt_order[3].score}     ({batt_order[3].balls_faced})  {batt_order[3].status}")
    print(Fore.GREEN, f"{batt_order[4].name}              {batt_order[4].score}     ({batt_order[4].balls_faced})   {batt_order[4].status}")
    print(Fore.GREEN, f"{batt_order[5].name}              {batt_order[5].score}     ({batt_order[5].balls_faced})   {batt_order[5].status}")
    #print("--------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------")
    print(Fore.BLUE,f"-----Team Total is {batt_order[0].score+ batt_order[1].score+batt_order[2].score+batt_order[3].score+batt_order[4].score+batt_order[5].score}--------")
    print("--------------------------------------------------------------------------------------------------")
    #print("--------------------------------------------------------------------------------------------------")
def print_pool(pool_of_players):
    for ii in pool_of_players:
        print(Fore.BLUE,ii.name)
def print_bat_order(pool_of_players):
    jj=1
    for ii in pool_of_players:
        print(f"{jj}.{ii.name}")
        jj=jj+1



#------------------------------------------Game Starts--------------------------------------------

print("We are going to Play a lovely game of cricket.......")
print(f"These are the current players in the squad....")
print_pool(pool_of_players)

user_in=input("Do you want to add any player:")
while user_in=="y":
    add_player()
    print(f"These are the current players in the squad....")
    print_pool(pool_of_players)
    user_in = input("Do you want to add any player:")

batt_order=bat_order()
print("This is the batting Order")
print_bat_order(batt_order)
no_of_balls1 = input("Please enter the no of Balls per match: ")
while no_of_balls1.isnumeric()==False:
    print("Entry not Valid, Enter a Valid number")
    no_of_balls1 = input("Please enter the no of Balls per match: ")

no_of_balls=int(no_of_balls1)
playmatch(no_of_balls,batt_order)
print_scorecard()

