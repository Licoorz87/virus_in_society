from creationPopulation import createPopulation
from creationVirus import creationName, creationProperties
from random import random, randint
from os import system
import matplotlib.pyplot as plt

# Print Pretty
def clear():
	# Pycharm / Pydroid
	try:
		system('clear')
	except:
		pass

	# CMD / VSCode
	try:
		system('cls')
	except:
		pass


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

infectedDays = list()
immunizedDays = list()
deadDays = list()

# main
day = 0
infectedPerMutation = 0
while infected != 0:
	# Per day
	infectedToday = 0
	immunizedToday = 0
	deadToday = 0
	
	#son = [i, False, risk, 0, []]
	for number, person in enumerate(population):
		if person[1] == True:
			lethalityPerson = lethality + (1 * person[2]) / (maxActiveTime - incubationTime)
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
				contacts = randint(3, 5)
				
				for contact in range(contacts):
					indexPerson = randint(0, len(population)-1)
					personContact = population[indexPerson]
					
					if personContact[1] == False:
						randomNumber = random() * 100
						
						if randomNumber <= transmissionTax:
							population[indexPerson][1] = person[1]
							infected += 1
							infectedToday += 1
	
	clear()
	print(f'day {day+1}')
	print('\nToday:')
	print(f'infected = {infectedToday}')
	print(f'immunized = {immunizedToday}')
	print(f'dead = {deadToday}')
	print('\nSince always:')
	print(f'infected = {infected}')
	print(f'immunized = {immunized}')
	print(f'dead = {dead}')
	day += 1
	infectedPerMutation += infectedToday

#	if infectedPerMutation > 1000:
#	infectedPerMutation -= 1000
#
#		randomNumber = randint(1, 10000)
#
#		if randomNumber < mutationRate:
#			for num, person in enumerate(population):
#				if person[1] == 'Immunized':
#					population[num][1] = False
#
#				immunized = 0


	infectedDays.append(infectedToday)
	immunizedDays.append(immunizedToday)
	deadDays.append(deadToday)


# Final Statistics
clear()
print(nameVirus)
listOfProperties = [transmissionTax, (dead * 100) / (immunized - dead), incubationTime, maxActiveTime, mutationRate]
nameOfProperties = ['transmission Tax (%)', 'lethality (%)', 'incubation Time', 'maxActiveTime', 'mutationRate (%)']

for number, property in enumerate(listOfProperties):
	print(f'{nameOfProperties[number]} = {property}')
	
print(f'\nday {day+1}')
print('\nSince always:')
print(f'Infected = {infected}')
print(f'immunized = {immunized}')
print(f'dead = {dead}')

graphics = input('Show Graphics? [Y/N]\n').upper()[0]

if graphics == 'Y':
	datas = [infectedDays, immunizedDays, deadDays]
	subtitlesData = ['Infected Per Day', 'Immunized Per Day', 'Dead Per Day']

	for num, data in enumerate(datas):
		fig, ax = plt.subplots()
		ax.plot([i for i in range(1, day+1)], data)
		ax.set(xlabel='Days', title='Counting of ' + subtitlesData[num])
		ax.grid(True)
		plt.show()
