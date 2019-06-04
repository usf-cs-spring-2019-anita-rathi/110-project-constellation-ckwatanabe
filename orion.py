#Christian Kotaro Watanabe
#Version 18
#May 24, 2019

# This program draws the constellation for Orion

import turtle
turtle.setup(500,500)

# prevents turtle fom drawing lines until specified to draw lines
turtle.penup()
turtle.hideturtle()

# Defining the star coordinates for Betelgeuese
bet_X = -70
bet_Y = 200
turtle.goto(bet_X, bet_Y)
turtle.dot(5) #Draws the dot for the star
turtle.write('Betegeuse') #Writes the star name

# Defining the star coordinates for Meissa
mei_X = 80
mei_Y = 180
turtle.goto(mei_X, mei_Y)
turtle.dot(5) #Draws the dot for the star
turtle.write('Meissa') #Writes the star name

# Defining the star coordinates for Alnitak
aln_X = -40
aln_Y = -20
turtle.goto(aln_X, aln_Y)
turtle.dot(5) #Draws the dot for the star
turtle.write('Alnitak') #Writes the star name

# Defining the star coordinates for Alnilam
alnil_X = 0
alnil_Y = 0
turtle.goto(alnil_X, alnil_Y)
turtle.dot(5) #Draws the dot for the star
turtle.write('Alnilam') #Writes the star name

# Defining the star coordinates for Mintaka
mint_X = 40
mint_Y = 20
turtle.goto(mint_X, mint_Y)
turtle.dot(5) #Draws the dot for the star
turtle.write('Mintaka') #Writes the star name

# Defining the star coordinates for Saiph
sai_X = -90
sai_Y = -180
turtle.goto(sai_X, sai_Y)
turtle.dot(5) #Draws the dot for the star
turtle.write('Saiph') #Writes the star name

# Defining the star coordinates for Rigel
rig_X = 120
rig_Y = -140
turtle.goto(rig_X, rig_Y)
turtle.dot(5) #Draws the dot for the star
turtle.write('Rigel') #Writes the star name

#This next section of code is to connect the stars with lines

# Draws a line from Betelgeuse to Alnitak
turtle.goto(bet_X, bet_Y)
turtle.pendown() #allowing the turtle to draw lines
turtle.goto(aln_X, aln_Y)
turtle.penup() #preventing the turtle from drawing lines

# Draws only a line from Meissa to Mintaka
turtle.goto(mei_X, mei_Y)
turtle.pendown() #allowing the turtle to draw lines
turtle.goto(mint_X, mint_Y)
turtle.penup() #preventing the turtle from drawing lines

# Draws only a line from Alnitak to Alnilam
turtle.goto(aln_X, aln_Y)
turtle.pendown() #allowing the turtle to draw lines
turtle.goto(alnil_X, alnil_Y)
turtle.penup() #preventing the turtle from drawing lines

# Draws only a line from Alnilam to Mintaka
turtle.goto(alnil_X, alnil_Y)
turtle.pendown() #allowing the turtle to draw lines
turtle.goto(mint_X, mint_Y)
turtle.penup() #preventing the turtle from drawing lines

# Draws only a line from Alnitak to Saiph
turtle.goto(aln_X, aln_Y)
turtle.pendown() #allowing the turtle to draw lines
turtle.goto(sai_X, sai_Y)
turtle.penup() #preventing the turtle from drawing lines

# Draws only a line from Mintaka to Rigel
turtle.goto(mint_X, mint_Y)
turtle.pendown() #allowing the turtle to draw lines
turtle.goto(rig_X, rig_Y)
turtle.penup() #preventing the turtle from drawing lines

#Signifying end of program
turtle.done()
