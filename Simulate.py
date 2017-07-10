import os, random, time, sys, Tidepool, Tadpole, Tile
from namegen import name_cvcv, name_cvcvc, name_gen
from Tidepool import *
from Tadpole import *
from Tile import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


def fights(countme):
	Fights = [Tadpole(0,0), Tadpole(0,0)]

	for x in range(countme):
    		if ((Fights[0].contemplate(Fights[1])) > 50):
			print Fights[0].name + " defeats " + Fights[1].name + " and advances "
			Fights[1] = Tadpole()
    		else:
			print Fights[1].name + " defeats " + Fights[0].name + " and advances "
        		Fights[0] = Tadpole()
    
		Fights[0].show_skills()
		Fights[1].show_skills() 

#fights(100)

john = Tidepool()
print "Population: " + str(john.population)
john.show_tidepool()
#john.print_life()

turns = 1

for i in range(turns):
	john.take_turn()
	john.tadpoles_go()
	john.show_tidepool()
	time.sleep(.2)

#poolo.show_tidepool()

'''
#makes a 5x5 list of tadpoles (first var must be n+1)
yloc = []
xloc = []

for i in range(6):
	#nesting lists in a list
	yloc.append(xloc)
	xloc = []
	for x in range(5):
		#if(random.randint(0,4) > 3):
		xloc.append(Tadpole())



'''
