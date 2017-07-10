#!/usr/bin/python
import os, random

vowel = ["a", "e" , "i" , "o", "u" ]
const = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

#Input: Structure of a word
#Output: Word generated from said structure
def name_gen():

	new_name = ""

	for x in range( int(10) ): #This algo uses 1/3 vowel and 2/3 consts

		if ( (random.random() * 3) > 1):
			new_name += const[int( len(const) * random.random())] 
		else:
			new_name += vowel[int( len(vowel) * random.random())]

	return new_name

def name_cvcv():
	#name_cvcv = ""
	return (add_const() + add_vowel() + add_const() + add_vowel() )

def name_cvcvc():
	#name_cvcv = ""
	return (add_const() + add_vowel() + add_const() + add_vowel() + add_const() )


#Generates a word sructure in the form of a boolean string
def word_struc():

	cvcc = ""

	cvcc += add_const()
	cvcc += add_vowel()
	cvcc += add_const()
	cvcc += add_const()

	return cvcc

#adds a vowel
def add_vowel():
	v = vowel[(int(len(vowel)  * random.random()))]
	return v


#adds a constonant
def add_const():
	c = const[(int(len(const)  * random.random()))]
	return c
