import os, random, sys, time, math, Tadpole, Tile, colorama 
from namegen import name_cvcv, name_cvcvc, name_gen
from Tadpole import *
from Tile import *

'''
# Tidepool holds a number of Tadpoles which evolve
# Every "generation" is divided into steps
# Food is delivered to meet the needs of 80-90% of the population
# Tadpoles must fight to eat and reproduce
# Tadpoles may have children who must grow up (and are weaker at birth)
#
# Tidepool holds a list of space objects
# Space objects can hold a tadpole or food object

	Enviromental influence
	----------------------
	voltility: A higher volitility means more fish and natural threats will kill Tadpoles
        population: The number of Tadpoles to be spawned within the tidepool
	Size: !!!!
	food_supply: The amount of food designated for the population
	
	
	Understanding Space
	-------------------
	explains how to view the tidepool and print it

'''


class Tidepool():

        #combat_log(attacker,defender,number,option)
        #show_tidepool(self)
	#what(x,y) returns the object at location x,y

	def __init__(self):	
	    self.volitility = random.randint(50,100)
	    self.population = 5 #random.randint(3,5)
	    self.food = int(self.population * .4)

	    print "Vol: " + str(self.volitility)
   	    print "Pop: " + str(self.population)
   	    print "Fod: " + str(self.food)
	    
	    #self.center_tile

	    self.list_life = []
	    self.list_food = []
	    self.list_kelp = []

	    self.yloc = []
	    xloc = []  
	  
            self.height = 16 #refers to yloc   36 is max
	    self.width  = 16 #refers to xloc

	    '''
	    Mitchels best canidate algorithm
	    Pre-1. Start somewhere and remember its place
	    assume N[] to be a list of existing points		
	    1. Select n random points (10 seems healthy).
	    2. Compare each random point to N[] and the point with the average furthest
	    distance away is created. Repeat until population_count = 0

	    for this its
		1. make everything a tile()
		2. ovverride one tile with Tadpole()
		3. run mitchels algorithm %population_size% times
		4. run mitchels n times for kelp (altered)
		5. run mitchels n times for food (altered)
	    '''
	    
	    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
		### MITCHELLS ALGORITHM ### TADPOLE POPULATION ###
	    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	    #Sets up the premise of all tiles
	    for i in range(self.height):
	       	xloc = []
	        for x in range(self.width):
			xloc.append(Tile(i,x))
                self.yloc.append(xloc)


	    #Creates a tadpole randomly somewhere
            self.list_life.append(Tadpole(random.randint(0,(self.width - 1)),random.randint(0,(self.height - 1))))

	    #Actually adds it to the Tidepool (yloc)
	    (self.yloc[((self.list_life[0]).location_y)])[((self.list_life[0]).location_x)] = self.list_life[0] 

		###ERROR CAUSED BY MULTIPLE BROS ON 0,0
            	
            #Accounts for the already generated tadpole
	    while( len(self.list_life) < self.population ):
		    #print "RUNS " + str(x) + " TIMES"	
		    best_x = 0
		    best_y = 0			
		    greatest_index = -1     	    
  		    possible_pts = [] #empty list for possible points
	            len_pts = [] #holds the lens for possible points		   
		    i = 0

		    cen_tile_x = ((self.width) / 2) 
	            cen_tile_y = ((self.height) / 2)
		
		    n = 2 #How many random points to generate
		    q = 10 #number of offsets to pull out tadpoles

		    #fix ideas: add q extra points to pull tadpole generation from the outskirts

		    #where n = i < n
                    while(i < n):
				#randomly copies a point and adds it to possible_pts
				possible_pts.append((self.yloc[random.randint(0,(self.height - 1))])[random.randint(0,(self.width - 1))]) 

				#if the point is a tile then i++
				if((possible_pts[i]).symbol == "-"):
					#print str(possible_pts[i].location_x) + "," + str(possible_pts[i].location_y)
					i += 1
				#else it MUST be taken by something else, so it is removed
				else:
					possible_pts.remove(possible_pts[i])

		    for i in range(q):

			if((self.yloc[cen_tile_y])[cen_tile_x].symbol == "-"):
				possible_pts.append((self.yloc[cen_tile_y])[cen_tile_x])
			else:
				cen_tile_x += 1
			

		    #compares a possible point to ALL tadpoles and finds average distance
		    for i in range(len(possible_pts)):
					
			distance = 0.0 #holds the largest avg. number to find "winner"		
			y = 0

			#for y in list_life, add the distance (and at the end divide by len()) 
			while(y < len(self.list_life)):

				left = abs(float((self.list_life[y]).location_y - (possible_pts[i]).location_y)) 
				right = abs(float((self.list_life[y]).location_x - (possible_pts[i]).location_x))

				#Distance formula 
				distance += math.sqrt((left * left) + (right * right)) 
				#print "Num generates avg" + str(greatest)
				y += 1	

			#finds the average distance
			len_pts.append(distance / float(len(self.list_life))) 
			#print "Average added: " + str(len_pts[i])
			
		    #finds the max
		    for i in range(len(len_pts)):
			if(len_pts[i] == max(len_pts)):
				best_x = (possible_pts[i]).location_x
				best_y = (possible_pts[i]).location_y


		    #its possible that spaces dont exist once population is higher in small grids	  
		    try:  
		      if ( (self.yloc[best_y])[best_x].symbol == "-"):
			
	 		if ( ((self.yloc[(best_y - 1)])[(best_x - 1)].symbol == "-") and ((self.yloc[(best_y - 1)])[best_x].symbol == "-")):		
			    if ( ((self.yloc[(best_y - 1)])[(best_x + 1)].symbol == "-") and ((self.yloc[best_y])[(best_x - 1)].symbol == "-")):
 				
				if ( ((self.yloc[best_y])[(best_x + 1)].symbol == "-") and ((self.yloc[(best_y + 1)])[(best_x - 1)].symbol == "-")):
			 				
				    if ( ((self.yloc[(best_y + 1)])[(best_x + 1)].symbol == "-") ):

		    			#A Tadpole is made in the best possible location
		    			(self.yloc[best_y])[best_x] = Tadpole(best_x, best_y)

					#appends the new Tadpole to list_life
	         			self.list_life.append((self.yloc[best_y])[best_x])
		    except:
		    	pass		
			####ACCOUNT FOR GENDER BASED ON SURROUNDINGS lATER
 
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
		### END MITCHELLS ### TADPOLE POPULATION ###
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
		### FOOD GEN START ###
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	    #just in case the center is a Tadpolio
	    if( (self.yloc[cen_tile_y])[cen_tile_x].symbol != "-"): cen_tile_x += 1


	    while( len(self.list_food) < self.food):

		#generate a food tile somewhere near the average of all tadpoles?
		#place n foods around the %MEAN tile however let tadpoles all have equal chance 
		#by offsetting larger amounts of food nearer more # of tadpolios
		x = random.randint( int(-(self.width / 4.0))  , int((self.width / 4.0))  )
		y = random.randint( int(-(self.height / 4.0)) , int((self.height / 4.0)) )		

		if( (self.yloc[(cen_tile_y + y)])[(cen_tile_x + x)].symbol == "-"):
			(self.yloc[(cen_tile_y + y)])[(cen_tile_x + x)].set_food()
			self.list_food.append( (self.yloc[(cen_tile_y + y)])[(cen_tile_x + x)] )

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
		### FOOD GEN END ###
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#




	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
		### KELP GEN START ###
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	#for kelp I should try something like a random tree distrobution
	#where is has a % to grow a certain direction but will eventually be cut off

	    while(len(self.list_kelp) < int(self.population * 2.0)):
		
		x = random.randint( int(-(self.width / 2.5))  , int((self.width / 2.5))  )
		y = random.randint( int(-(self.height / 2.5)) , int((self.height / 2.5)) )		

		
		if ((self.yloc[(cen_tile_y + y)])[(cen_tile_x + x)].symbol == "-"): #if its empty
			(self.yloc[(cen_tile_y + y)])[(cen_tile_x + x)].set_kelp()	
			self.list_kelp.append((self.yloc[(cen_tile_y + y)])[(cen_tile_x + x)])

	    original_kelps = len(self.list_kelp)

	    for i in range(original_kelps):
	
		grow_chance = 30

		while(grow_chance > 0):
	
			x = (self.list_kelp[i]).location_x + random.randint(-1,1)
			y = (self.list_kelp[i]).location_y + random.randint(-1,1)

			try:
				if( (self.yloc[y])[x].symbol == "-"):
					(self.yloc[y])[x].set_kelp()
					self.list_kelp.append((self.yloc[y])[x])
	
				else:
					grow_chance -= 10
			except:
				pass

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
		### KELP GEN END ###
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



	
	def take_turn(self):
		
	    #for every tadpole calculate a list of "action" objects and sort them.
            for i in range(len(self.list_life)):

	      # up left , up up , up right : left , right : down left , down down , down right
	      sight = [1,1,1,1,1,1,1,1]

	      #print "Tadpole " + self.list_life[i].name + " observes the surroundings..."

	      for y in range(self.list_life[i].perception): 

	          for x in range(self.list_life[i].perception): 	

		    if( sight[0] == 1):
       		      #empty kelp + stop searching
		      try:
    		        if( (self.yloc[((self.list_life[i]).location_y + y)])[((self.list_life[i]).location_x + x)].symbol == "K"):
			  self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y + y)])[((self.list_life[i]).location_x + x)])
		          sight[0] = 0

   			self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y + y)])[((self.list_life[i]).location_x + x)])

		      except:
		      	  sight[0] = 0
	
		    if( sight[1] == 1):
       		      #empty kelp + stop searching
		      try:
    		        if( (self.yloc[((self.list_life[i]).location_y - y)])[((self.list_life[i]).location_x - x)].symbol == "K"):
			  self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y - y)])[((self.list_life[i]).location_x - x)])
		          sight[0] = 0

   			self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y - y)])[((self.list_life[i]).location_x - x)])

		      except:
		      	  sight[0] = 0
	
		    if( sight[2] == 1):
       		      #empty kelp + stop searching
		      try:
    		        if( (self.yloc[((self.list_life[i]).location_y - y)])[((self.list_life[i]).location_x)].symbol == "K"):
			  self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y - y)])[((self.list_life[i]).location_x)])
		          sight[0] = 0

   			self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y - y)])[((self.list_life[i]).location_x)])

		      except:
		      	  sight[0] = 0
	
		    if( sight[3] == 1):
       		      #empty kelp + stop searching
		      try:
    		        if( (self.yloc[((self.list_life[i]).location_y - y)])[((self.list_life[i]).location_x + x)].symbol == "K"):
			  self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y - y)])[((self.list_life[i]).location_x + x)])
		          sight[0] = 0

   			self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y - y)])[((self.list_life[i]).location_x + x)])

		      except:
		      	  sight[0] = 0
	
		    if( sight[4] == 1):
       		      #empty kelp + stop searching
		      try:
    		        if( (self.yloc[((self.list_life[i]).location_y)])[((self.list_life[i]).location_x - x)].symbol == "K"):
			  self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y)])[((self.list_life[i]).location_x - x)])
		          sight[0] = 0

   			self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y)])[((self.list_life[i]).location_x - x)])

		      except:
		      	  sight[0] = 0

		    if( sight[5] == 1):
       		      #empty kelp + stop searching
		      try:
    		        if( (self.yloc[((self.list_life[i]).location_y + y)])[((self.list_life[i]).location_x - x)].symbol == "K"):
			  self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y + y)])[((self.list_life[i]).location_x - x)])
		          sight[0] = 0

   			self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y + y)])[((self.list_life[i]).location_x - x)])

		      except:
		      	  sight[0] = 0
	
		    if( sight[6] == 1):
       		      #empty kelp + stop searching
		      try:
    		        if( (self.yloc[((self.list_life[i]).location_y + y)])[((self.list_life[i]).location_x)].symbol == "K"):
			  self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y + y)])[((self.list_life[i]).location_x)])
		          sight[0] = 0

   			self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y + y)])[((self.list_life[i]).location_x)])

		      except:
		      	  sight[0] = 0
	
		    if( sight[7] == 1):
       		      #empty kelp + stop searching
		      try:
    		        if( (self.yloc[((self.list_life[i]).location_y + y)])[((self.list_life[i]).location_x + x)].symbol == "K"):
			  self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y + y)])[((self.list_life[i]).location_x + x)])
		          sight[0] = 0

   			self.list_life[i].thoughts.append((self.yloc[((self.list_life[i]).location_y + y)])[((self.list_life[i]).location_x + x)])

		      except:
		      	  sight[0] = 0
	
              self.list_life[i].think()
	

	def tadpoles_go(self):

	    for i in range(len(self.list_life)):
		
	        if( (self.list_life[i].make_move())[0] == 1): #Moves a tadpole from a free space (changes personal coords)
		    try:
			#copies object that the tadpole wants to interact with
			temp = (self.yloc[((self.list_life[i].make_move())[1]).location_y])[((self.list_life[i].make_move())[1]).location_x]
			temp_x = temp.location_x
			temp_y = temp.location_y

			#copies the tadpole to the space it would like to move to
			(self.yloc[temp_y])[temp_x] = self.list_life[i]
				
			#copies temp where list_life still has tadpole
			(self.yloc[self.list_life[i].location_y])[self.list_life[i].location_x] = temp
	
                        #updates new tiles coordinates
 			(self.yloc[self.list_life[i].location_y])[self.list_life[i].location_x].location_x = self.list_life[i].location_x
		        (self.yloc[self.list_life[i].location_y])[self.list_life[i].location_x].location_y = self.list_life[i].location_y                    
			#updates tapoles location
			self.list_life[i].location_x = temp_x
			self.list_life[i].location_y = temp_y	

			self.list_life[i].clean_mind()
		    except:
			self.list_life[i].clean_mind() #might come back to bite my ass
			#takes returned best action and does it!
				

	def combat_log(attacker, defender, number, option):
		if option == 1:
    			print (attacker + " attacks " + defender + " and deals " + str(number) + " damage!")
  		if option == 2:
    			print (attacker + " attacks " + defender + " but the attack is dodged!")
  		if (option == 3):
  		  	print (attacker + " attacks " + defender + " and deals a killing blow!")
  		if (option == 4):
   			print (defender + " has " + str(number) + " HP remaining! ")


	def print_life(self):

		print "\nCurrent Population\n|~~~~~~~~~~~~~~~|"

		for i in range(len(self.list_life)):
			print " " + (self.list_life[i]).name + " : " + str((self.list_life[i]).location_x) + "," + str((self.list_life[i]).location_y)
		
		print "|~~~~~~~~~~~~~~~|\n"

        
	def show_tidepool(self):

		print(chr(27) + "[2J")
		print "~~~~"*(len(self.yloc)) 

  		for i in range(len(self.yloc)):
    			for x in range(len(self.yloc[i])):
				if ( (self.yloc[i])[x].symbol == "-"):
				    sys.stdout.write("\033[0;34m" + " -  " + "\033[0;32m")
				elif ( (self.yloc[i])[x].symbol == "K"):
				    sys.stdout.write("\033[0;32m" + " K  " + "\033[0;32m")
				elif ( (self.yloc[i])[x].symbol == "M"):
				    sys.stdout.write("\033[0;37m" + " M  " + "\033[0;32m")
			        elif ( (self.yloc[i])[x].symbol == "F"):
				    sys.stdout.write("\033[0;36m" + " F  " + "\033[0;32m")
				elif ( (self.yloc[i])[x].symbol == "#"):
				    sys.stdout.write("\033[0;31m" + " #  " + "\033[0;32m")
			print "\n"
	 
	


