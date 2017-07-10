import os, random, time
from namegen import name_cvcv, name_cvcvc, name_gen


'''
	A Tadpole can die from:
	1. Injuries in combat
	2. Having 0 health 
	3. Starving
	4. Reaching a certain age (Rfavored gaussian).
	
	Combat Stats
	------------
	Health: Used to take damage

	Attack: Used to deal damage

	Utility Stats
	--------------
	Speed: Used for movement calculations

	Injuries: A Tadpole might have injuries which take time to heal or leave scarring on their health pool. This
	usually sets the tadpole into death spiral.

	Decision Stats
	--------------
	Perception: Used when a tadpole makes judgement calls about fighting and moving, higher
	numbers means more a precise understanding of the enviroment.
	
	Aggression: Used when a tadpole makes judgement calls to fight other tadpoles, higher agression
	makes tadpoles defensive of territory and less likely to contest a resource.

	Hunger: A hungry tadpole will select food as an answer to their existential drives.

	Intelligence: Allows tadpoles to make better decisions to align themselves with the best possible gain for 
	survival, recource gain, and efficiency. Intelligent Tadpoles might try to run from combat or hide from
	more powerful tadpoles.

	Gender: This greatly effects behavior as males will seek out females and vice versa. Males will have (on average) a 
	higher aggression rating and females will have a higher hunger rating when breeding.
 

	Miscelaneous/Characteristics
	----------------------------
	Age: Used to document overall behavioral efficiency reguarding lifespan and behavior.
	Documented by turn age and Child/Adolescent/DeathSpiral. !!! To be added in a later version !!!

	Symbol: Used when displaying the Tadpole visually in terminal.
 
'''

class Tadpole():

	def __init__(self, x, y):
		if x is -1: #call factory methods
			self.location_x = -1
			self.location_y = -1
		else:
			self.location_x = x
			self.location_y = y
		
		if(random.randint(0,2) > 1):
			self.name = name_cvcv() #cvcv()
		else:
			self.name = name_cvcvc() #cvcvc()

		if(random.randint(0,2) > 1):
			self.gender = 1
			self.symbol = "M"
		else:
			self.gender = 0
			self.symbol = "F"

		# 0 = nothing 1 = eating 
		self.status = 0

		self.speed  = 1 + random.randint(-2,2)
		self.health = 20 + random.randint(-3,5)
		self.attack = 1 + random.randint(0,2)
		self.aggression = 80 + random.randint(-20,20)
		#also make it sleep
		self.perception = 2 #4 + random.randint(-1,1)
		self.age = 0
		self.hunger = 0
		self.on_kelp = 0

		self.stats = [ self.health , self.attack , self.attack ]		
				
		self.thoughts = []
		self.thought_weights = []

	def show_skills(self):
		print "Name:   " + self.name
		print "~~~~~~~~~~~~~~~~~"
		print "Speed:  " + str(self.speed)
		print "Health: " + str(self.health)
		print "Attack: " + str(self.attack)
 		print "~~~~~~~~~~~~~~~~~"
		print "Aggres: " + str(self.aggression) 
		print "Gender: " + str(self.symbol) 
		print "Percep: " + str(self.perception)
		print "Age:    " + str(self.age)
		print "Hunger: " + str(self.hunger) + "%"
		print "\n\n"


	def think(self):

		for i in range(len(self.thoughts)):
	
			#bigge vars, do I see food, mate, goal/directive?
	
		  #tadpole same gender?
		  try:
		    if( self.thoughts[i].gender == self.gender):
		      if(self.symbol == "M"): #mvm
		        self.thought_weights.append( ((contemplate(self, self.thoghts[i]) + self.agression) % 100)  )
		      else: #fvf
		        self.thought_weights.append( ((contemplate(self, self.thoghts[i]) + self.agression) % 100)  )

	            else: #tadpole opp gender
		      if(self.symbol == "M"): #mvf
		        self.thought_weights.append( (((contemplate(self, self.thoghts[i])) + self.agression) % 100) )
		      else: #fvm
		        self.thought_weights.append( ((contemplate(self, self.thoghts[i]) + self.agression) % 100)  )
	      			
		  except:
		    pass

		  try:
		    if (self.thoughts[i].symbol == "#"):
		      self.thought_weights.append(self.hunger)
		      #food
		      #am i hungry?

		  except:
		    pass			

		  try:
		    if(self.thoughts[i].symbol == "-"): #tadpoles can only move 1 space!
		      #which space is the closest to more stuff?
		      self.thought_weights.append(random.randint(0,5))
			#fix this too lazy ass			

		  except:
		    pass

		  try:
		    if(self.thoughts[i].symbol == "K"):
		      #am I in danger?
		      danger = 0			

		      for n in range(len(self.thoughts)):
		        try: #if its  a tadpole
			  danger += (self.thoughts[n].aggression + (self.contemplate(self , self.thoughts[n])) )
 			except: #if there is more kelp then you can run easier
			  if (self.thoughts[n].symbol == "K"):
			    danger -= 5

		      self.thought_weights.append(danger)

		  except:
		    pass

		  if( i == len(self.thought_weights)): #if something broke and nothing was added...
			self.thought_weights.append(0)


	#causes the tadpole to select the best move for itself
	#returns an action and object to recieve action [action, object]
	#1 = move
	def make_move(self):

	   best_idea = max(self.thought_weights)
	   best_idea_index = -1

	   for i in range(len(self.thought_weights)):

		if(self.thought_weights[i] == best_idea):
			best_idea_index = i

	   #fancy output for readability
	   if (self.thoughts[best_idea_index].symbol == "-"):
	      return [1, self.thoughts[best_idea_index]]
 
           elif(self.thoughts[best_idea_index].symbol == "K"):
	      print self.name + " would like to hide in nearby kelp"	  
	
           elif(self.thoughts[best_idea_index].symbol == "#"):
	      print self.name + " would like to eat some food"	  


	   #account for self.symbol == M	
	   elif( (self.thoughts[best_idea_index].symbol == "M") and (self.symbol == "F")):
	      print self.name + " wants to have sex with " + str(self.thoughts[best_idea_index].name)
	   else:
              print self.name + " wants to KILL " + str(self.thoughts[best_idea_index].name)


	   return [0, self]
	   ''' 
	   for i in range(len(self.thoughts)):

		   print self.name + " options look like " + str(self.thoughts[i])
		   print self.name + " options look like " + str(self.thought_weights[i])
	   '''

	def clean_mind(self):
	      self.thoughts = []
	      self.thought_weights = []


	def contemplate(self, Tadpole):
		
		print self.name + " contemplates fighting " + Tadpole.name
	
		simWin = 0

		for x in xrange(100):
			simWin += self.quiet_fight(Tadpole)
			
		print self.name + " has a " + str(simWin) + "% chance to kill " + Tadpole.name

		return int(simWin)

		
	def quiet_fight(self, Tadpole):
		#Used to track this instance of combat
		myPercep = (1 - ( (self.perception - 1) / self.perception) ) #allows tadpoles with higher percep
		myHealth = self.health
		enemyHealth = Tadpole.health
		turnDamage = 0
		
		while( (myHealth > 0) or (enemyHealth > 0) ):		
			myHealth -= Tadpole.stats[2] + random.randint((-3 * myPercep),(3 * myPercep))				
			enemyHealth -= self.stats[2] + random.randint((-3 * myPercep),(3 * myPercep))				

		if myHealth > enemyHealth:
			return 1
		else:
			return 0


	def fight(self, Tadpole):			
		print self.name + " prepares to fight " + Tadpole.name 

		#used to track combat
		myHealth = self.health
		enemyHealth = Tadpole.health
		turnDamage = 0
		
		if self.stats[0] > Tadpole.stats[0]:
			print self.name + " is faster and makes the first move!"
			fighters = [self.stats, Tadpole.stats]
		else:
			print Tadpole.name + " is faster and makes the first move!"
			fighters = [self.stats, Tadpole.stats]

		while( (myHealth > 0) or (enemyHealth > 0) ):
				#spd hp attk
			turnDamage = self.stats[2] + random.randint(-3,3)				

			#Friendly attack
			if( (enemyHealth - turnDamage) > 0 ):
				combat_log(self.name , Tadpole.name , turnDamage, 1)
				combat_log(self.name , Tadpole.name , (enemyHealth - turnDamage), 4)
			else:
				combat_log(self.name , Tadpole.name , turnDamage, 3)
				return 1 #win
	
			enemyHealth -= turnDamage

			#Enemy attack
			turnDamage = Tadpole.stats[2] + random.randint(-3,3)				

			if( (myHealth - turnDamage) > 0 ):
				combat_log(Tadpole.name, self.name , turnDamage, 1)
				combat_log(Tadpole.name, self.name , (myHealth - turnDamage), 4)
			else:
				combat_log(Tadpole.name, self.name , turnDamage, 3)
				return 0 #loss

			myHealth -= turnDamage
