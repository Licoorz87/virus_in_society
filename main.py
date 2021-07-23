from creationPopulation import createPopulation
from creationVirus import creationName, creationProperties
from random import random, randint
from os import system
from time import sleep

# Create virus and population
population = createPopulation(50000)
nameVirus = creationName()
transmissionTax, lethality, incubationTime, maxActiveTime, mutationRate = creationProperties()


# First patient
patientZero = randint(0, len(population)-1)
population[patientZero][1] = True


# Statistics
infected = 1
immunized = 0
dead = 0


# main
day = 0
while infected != 0:
	# Per day
	infectedToday = 0
	immunizedToday = 0
	deadToday = 0
	
	for number, person in enumerate(population):
		if person[1] == True:
			lethalityPerson = lethality + person[2] / (maxActiveTime - incubationTime)
			if person[3] > maxActiveTime:
				population[number][1] = 'Immunized'
				infected -= 1
				immunized += 1
				immunizedToday += 1
				continue
				
			randomNumber = random() * 100
			if randomNumber <= lethalityPerson:
				population.pop(number)
				
				infected -= 1
				dead += 1
				deadToday += 1
				
			population[number][3] += 1
			
			if incubationTime <= person[3] <= maxActiveTime:
				contacts = randint(3, 7)
				
				for contact in range(contacts):
					indexPerson = randint(0, len(population)-1)
					personContact = population[indexPerson]
					
					if personContact[1] == False:
						randomNumber = random() * 100
						
						if randomNumber <= transmissionTax:
							population[indexPerson][1] = True
							infected += 1
							infectedToday += 1
	
	system('clear')
	print(f'day {day+1}')
	print('\nToday:')
	print(f'infected = {infectedToday}')
	print(f'immunized = {immunizedToday}')
	print(f'dead = {deadToday}')
	print('\nSince always:')
	print(f'infected = {infected}')
	print(f'immunized = {immunized}')
	print(f'dead = {dead}')
	#input()
	sleep(0.1)
	day += 1


# Final Statistics
system('clear')
print(nameVirus)
listOfProperties = [transmissionTax, lethality * (maxActiveTime - incubationTime), incubationTime, maxActiveTime, mutationRate]
nameOfProperties = ['transmission Tax', 'lethality', 'incubation Time', 'maxActiveTime', 'mutationRate (%)']

for number, property in enumerate(listOfProperties):
	print(f'{nameOfProperties[number]} = {property}')
	
print(f'\nday {day+1}')
print('\nSince always:')
print(f'Infected = {infected}')
print(f'immunized = {immunized}')
print(f'dead = {dead}')