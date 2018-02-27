#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

retter = ['Spaghetti Bologenese',
		 'Pizza',
		 'Lasagne',
		 'Burger',
		 'Pitabrød',
		 'Nachos',
		 'Tacokväll',
		 'Just Eat',
		 'Saag Paneer',
		 'Broccolitærte',
		 'Kartoffelsuppe',
		 'Panini',
		 'Spaghetti Cabonara',
		 'Rugbrød med lakserillette',
		 'Kartoffelmos med millionbøf',
		 'Keema korma',
		 'Tomat/peberfrugtsuppe',
		 'Pasta med tomatflødesovs',
		 'Pizzasnegle',
		 'Empanadas',
		 'Flødekartofler og mørbradbøf',
		 'Jordskokkesuppe',
		 'Bøf bearnaise',
		 'Gulerodssuppe',
		 'Sushi',
		 'Cannelloni',
		 'Risotto med svampe',
		 'Pulled pork',
		 'Risotto med spinat',
		 'Tortillas',
		 'Pizza med ricotta og kartoffel'
		 'Græskinspireret quesedillas',
		 'Spanakopita',
		 'Tærte med hakket oksekød',
		 'Langtidssimret oksekød med ris'
		 'Minestrone',
		 'Madpandekager med kødsovs',
		 'Roastbeef med hasselback-kartofler',
		 'Gnocci med spinatsovs']

random_numbers = []

date = 1

print "Der er %s retter i kogebogen." % len(retter)

while len(random_numbers) < len(retter):
	x = randint(0,(len(retter)-1))
	if x not in random_numbers and date < 32:
		print "%s.: %s" % (date, retter[x])
		random_numbers.append(x)
		date = date + 1
		if date >= 32:
			break

