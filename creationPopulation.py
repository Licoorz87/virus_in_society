from random import randint

# 100 = 1%
dataYears = [[0, 4, 600, 0.03], [5, 9, 650, 0.03], [10, 14, 680, 0.03], [15, 19, 740, 0.05], [20, 24, 750, 0.06], [25, 29, 710, 0.07], [30, 34, 760, 0.09], [35, 39, 780, 0.1], [40, 44, 720, 0.12], [45, 49, 630, 0.15], [50, 54, 650, 0.25], [55, 59, 570, 0.4], [60, 64, 550, 0.7], [65, 69, 370, 1], [70, 74, 300, 1.2], [75, 79, 220, 1.5], [80, 84, 140, 2.5], [85, 95, 180, 4]]

dataHIV = [[0, 14, 10], [15, 19, 12], [20, 24, 157], [25, 39, 100], [40, 59, 19], [60, 95, 7]]

dataIMC = [[0, 9, 620, 100], [10, 14, 1030, 210], [15, 17, 1940, 670], [18, 24, 3370, 1610], [25, 39, 5000, 2500], [40, 59, 7030, 2650], [60, 95, 3920, 1180]]

dataHeart = [[0, 24, 100], [25, 34, 43], [35, 44, 306], [45, 54, 466], [55, 64, 1000], [65, 95, 1982, 1711]]

dataDiabetes = [[0, 17, 5], [18, 29, 6], [30, 59, 50], [60, 64, 145], [65, 74, 199], [75, 95, 196]]

dataDiabetesInObesity = [8500, 1300]


def defineYears():
	maximum = 0
	for data in dataYears:
		maximum += data[2]
		
	randomNumber = randint(1, maximum)
	
	for data in dataYears:
		if randomNumber <= data[2]:
			yearsOld = randint(data[0], data[1])
			risk = data[3]
			break
			
		else:
			randomNumber -= data[2]

	return yearsOld, risk
	

def defineHIV(yearsOld):
	for data in dataHIV:
		if data[0] <= yearsOld <= data[1]:
			randomNumber = randint(1, 10000)
			
			if randomNumber <= data[2]:
				hivTest = True
				
			else:
				hivTest = False
				
			break
	
	return hivTest
	
	
def defineDiabetes(yearsOld):
	randomNumber = randint(1, 10000)
	
	for data in dataDiabetes:
		if data[0] <= yearsOld <= data[1]:
			if randomNumber <= data[2]:
				diabetes = True
			
			else:
				diabetes = False
			
			break
	
	return diabetes
	
	
def defineIMC(yearsOld, diabetes):
	if diabetes is True:
		randomNumber = randint(1, 10000)
		
		data = dataDiabetesInObesity.copy()
		if randomNumber <= data[0]:
			weight = 2
				
		elif randomNumber - data[0] <= data[1]:
			weight = 1
				
		else:
			weight = 0
				
		return weight

	randomNumber = randint(1, 10000)
	
	weight = 0
	for data in dataIMC:
		if data[0] <= yearsOld <= data[1]:
			if randomNumber <= data[2]:
				weight = 1
		
			break
	
	if weight == 0:
		maximum = 10000 - data[2]
		randomNumber = randint(1, maximum)
	
		for data in dataIMC:
			if data[0] <= yearsOld <= data[1]:
				if randomNumber <= data[3]:
					weight = 2
					break


	return weight


def defineHeart(yearsOld, diabetes):
	if diabetes is True:
		randomNumber = randint(1, 10000)
		
		if randomNumber <= 7800:
			heartTrouble = True
			
		else:
			heartTrouble = False
			
		return heartTrouble
		
	for data in dataHeart:
		if data[0] <= yearsOld <= data[1]:
			randomNumber = randint(1, 10000)
			
			if randomNumber <= data[2]:
				heartTrouble = True
				
			else:
				heartTrouble = False
				
			break
	
	return heartTrouble
	

def defineBreathing(yearsOld):
	if yearsOld < 5:
		breathing = 140
	
	else:
		breathing = 28 * yearsOld
		
	randomNumber = randint(1, 10000)	
	
	
	if randomNumber <= breathing:
		randomNumber = randint(1, breathing)
		
		if randomNumber <= breathing / 1.2:
			breathingResult = 1
		
		else:
			breathingResult = 2
		
	else:
		breathingResult = 0
		
	
	return breathingResult
	

def createPopulation(num):
	population = []

	for i in range(num):
		risk = 0
		
		yearsOld, riskYearsOld = defineYears()
		risk += riskYearsOld
		
		if defineHIV(yearsOld):
			risk += 3
		
		diabetes = defineDiabetes(yearsOld)
		if diabetes:
			risk += 1.05
		
		weight = defineIMC(yearsOld, diabetes)
		if weight == 1:
			risk += 0.15
		
		elif weight == 2:
			risk += 0.58
		
		if defineHeart(yearsOld, diabetes):
			risk += 1
			
		breathing = defineBreathing(yearsOld)
		if breathing == 1:
			risk += 0.3
		
		elif breathing == 2:
			risk += 1.5
		
		
		person = [i, False, risk, 0, []]
		
		population.append(person)
		
	return population
