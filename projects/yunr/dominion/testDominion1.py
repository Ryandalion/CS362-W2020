# -*- coding: utf-8 -*-
"""
Created on Thursday January 16th, 2020 at 8:05 PM

@author: Ryan Yun (yunr)
"""

import Dominion
import testUtility

trash = testUtility.initialize_trash()

#player_list = testUtility.retrieve_names()
player_list = ["Test User"];

nV, nC = testUtility.calculate_cards(player_list)

players = testUtility.create_player(player_list)

new_box = testUtility.create_box(nV)

supply_order = testUtility.create_supply_order()

used_box = testUtility.intialize_supply_box(new_box)

supply = testUtility.fill_supply(used_box, nV, nC, player_list)



#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)