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


john = Tidepool()
print "Population: " + str(john.population)
john.show_tidepool()


turns = 1

for i in range(turns):
	john.take_turn()
	john.tadpoles_go()
	john.show_tidepool()
	time.sleep(.2)
