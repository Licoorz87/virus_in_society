from creationPopulation import createPopulation
from creationVirus import creationName, creationProperties
from random import random, randint, vonmisesvariate
from os import system
import matplotlib.pyplot as plt
from sys import platform


class Virus:
	def __init__(self, name, transmission, lethality, incubationTime, maxActiveTime, mutationRate):
		self.name = name
		self.transmission = transmission
		self.lethality = lethality
		self.incubationTime = incubationTime
		self.maxActiveTime = maxActiveTime
		self.mutationRate = mutationRate

	def name(self):
		return self.name

	def transmission(self):
		return self.transmissionTax

	def lethality(self):
		return self.lethality
	
	def incubationTime(self):
		return self.incubationTime

	def maxActiveTime(self):
		return self.maxActiveTime

	def mutationRate(self):
		return self.mutationRate


# Print Pretty
def clear():
	if platform[0] == 'w':
		system('cls')

	elif platform[0] == 'l':
		system('clear')

	else:
		print('Operational System Not Found')
		exit()


numberOfPopulation = 100000

# Create virus and population
population = createPopulation(numberOfPopulation)
nameVirus = creationName()
transmission, lethality, incubationTime, maxActiveTime, mutationRate = creationProperties()
virusOrigin = Virus(nameVirus, transmission, lethality, incubationTime, maxActiveTime, mutationRate)

# First patient
patientZero = randint(0, len(population)-1)
population[patientZero][1] = virusOrigin


# Statistics
infected = 1
healthy = numberOfPopulation - 1
dead = 0

infectedDays = list()
healthyDays = list()
deadDays = list()
infectedSum = list()
healthySum = list()
deadSum = list()

# main
day = 0
infectedToMutation = 0
mutation = 0
while infected != 0:
	# Per day
	infectedToday = 0
	healthyToday = 0
	deadToday = 0
	
	for number, person in enumerate(population):
		if person[1] != False:
			lethalityPerson = person[1].lethality + (1 * person[2]) / (person[1].maxActiveTime - person[1].incubationTime)
			if person[3] > person[1].maxActiveTime:
				population[number][4].append(person[1].name)
				population[number][1] = False
				population[number][3] = 0
				infected -= 1
				healthy += 1
				healthyToday += 1
				continue
				
			population[number][3] += 1
			
			if person[1].incubationTime <= person[3] <= person[1].maxActiveTime:
				contacts = randint(3, 6)
				
				for contact in range(contacts):
					indexPerson = randint(0, len(population)-1)
					personContact = population[indexPerson]
					immunity = 0
					if len(personContact[4]) > 0:
						immunity += len(personContact)
					
					if personContact[1] == False:
						randomNumber = random() * 100
						
						if randomNumber <= person[1].transmission:
							if person[1].name not in personContact[4]:
								infected += 1
								infectedToday += 1
								infectedToMutation += 1
								healthy -= 1


								if infectedToMutation > 10000:
									infectedToMutation -= 10000

									randomNumber = randint(1, 100)

									if randomNumber < person[1].mutationRate:
										mutation += 1
										nameVirus = creationName()
										transmission, lethality, incubationTime, maxActiveTime, mutationRate = creationProperties()
										newVirus = Virus(nameVirus, transmission, lethality, incubationTime, maxActiveTime, mutationRate)
										population[indexPerson][1] = newVirus

									else:
										population[indexPerson][1] = person[1]
								
								else:
									population[indexPerson][1] = person[1]

			randomNumber = random() * 100
			if randomNumber <= lethalityPerson:
				population.pop(number)
				
				infected -= 1
				dead += 1
				deadToday += 1
	
	clear()
	print(f'day {day+1}')
	print('\nToday:')
	print(f'infected = {infectedToday}')
	print(f'healthy = {healthyToday}')
	print(f'dead = {deadToday}')
	print('\nSince always:')
	print(f'infected = {infected}')
	print(f'healthy = {healthy}')
	print(f'dead = {dead}')
	day += 1


	infectedDays.append(infectedToday)
	healthyDays.append(healthyToday)
	deadDays.append(deadToday)

	infectedSum.append(infected)
	healthySum.append(healthy)
	deadSum.append(dead)


# Final Statistics
clear()
listOfProperties = [virusOrigin.name, virusOrigin.transmission, (dead * 100) / numberOfPopulation, 
					virusOrigin.incubationTime, virusOrigin.maxActiveTime, virusOrigin.mutationRate]

nameOfProperties = ['name', 'transmission Tax (%)', 'mortality (%)', 'incubation Time', 'maxActiveTime', 'mutationRate (%)']

for number, property in enumerate(listOfProperties):
	print(f'{nameOfProperties[number]} = {property}')
	
print(f'\nday {day+1}')
print('\nSince always:')
print(f'Infected = {infected}')
print(f'healthy = {healthy}')
print(f'dead = {dead}')
print(mutation)

if healthy > 99900:
	exit()

graphics = input('Show Graphics? [Y/N]\n').upper()[0]

if graphics == 'Y':
	datas = [infectedDays, healthyDays, deadDays]
	subtitlesData = ['Infected In Day', 'healthy In Day', 'Dead In Day']
	colorName = ['red', 'blue', 'gray']

	fig, ax = plt.subplots(1, 3)
	for num, data in enumerate(datas):
		ax[num].plot([i for i in range(1, day+1)], data, color=colorName[num])
		ax[num].set(xlabel='Days', title=subtitlesData[num])
		ax[num].grid(True)
	
	plt.show()


	datas = [infectedSum, healthySum, deadSum]
	subtitlesData = ['Infected Per Day', 'healthy Per Day', 'Dead Per Day']
	colorName = ['red', 'blue', 'gray']

	fig, ax = plt.subplots(1, 3)
	for num, data in enumerate(datas):
		ax[num].plot([i for i in range(1, day+1)], data, color=colorName[num])
		ax[num].set(xlabel='Day', title=subtitlesData[num])
		ax[num].grid(True)
	
	plt.show()