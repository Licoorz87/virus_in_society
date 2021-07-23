from random import randint
from math import log
from os import system

def creationName():
	syllables = ['a', 'e', 'i', 'o', 'u', 's', 'r', 'm', 'ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci', 'co', 'cu', 'da', 'de', 'di', 'do', 'du', 'fa', 'fe', 'fi', 'fo', 'fu', 'ga', 'ge', 'gi', 'go', 'gu', 'ja', 'je', 'ji', 'jo', 'ju', 'la', 'le', 'li', 'lo', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu', 'qua', 'que', 'qui', 'quo', 'ra', 're', 'ri', 'ro', 'ru', 'sa', 'se', 'si', 'so', 'su', 'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'vu', 'za', 'ze', 'zi', 'zo', 'zu']
	
	sizeName = randint(3, 5)
	virusName = list()
		
	for i in range(sizeName):
		if i == 0:
			x = randint(8, len(syllables)-1)
			
		else:
			x = randint(0, len(syllables)-1)
			
		virusName.append(syllables[x])
			
	virusName = ''.join(virusName)
		
	return virusName
	

def creationProperties():
	transmissionFee = log(randint(2, 16), 2)
	incubationTime = randint(3, 10)
	activeTime = randint(7, 15)
	maxActiveTime = activeTime + incubationTime
	lethality = 0.99**randint(-178, 900)
	mutationRate = 0.99**(randint(-415, 415))
	
	return transmissionFee, lethality, incubationTime, maxActiveTime, mutationRate
