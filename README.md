# virus_in_society

It is a program with the purpose of being a virus simulator in a society, created with pre-defined standards.

the population is based on real data on age, HIV, diabetes, weight, heart problems and respiratory problems.

the virus has one name, a transmission rate, lethality, incubation time, active time and a probability of mutation every 10000 transmissions (all randomly).


• How Works?

The application works with three non-interactive programs: creationPoPulation.py, creationVirus.py and main.py.

1. creationPopulation - Creates a whole population with real data from the Brazilian population, such as: percentage of the population in a given age group, percentage of an age group with HIV, percentage of diabetes in an age group, and more.
In addition, the person's risk is calculated, this means if it is most likely to die than healthier other.

2. creationVirus - Creates a random virus. A name is created, the percentage of virus transmission, the percentage of lethality, the time of the inactive virus in the body, the time of the active virus in the body and the percentage of random mutation of the virus every 10000 transmissions.

3. main - This makes the whole process behind virus transmissions, deaths, mutation and everything else. First a population with 100,000 individuals (alterable) is created. Then the totally random virus is created, but may be modified.
After all created, the patient zero is randomly infected and the contagion begins.
Always showing the statistics of the day and the general statistics of infected, immunized and dead.
In the end, it uses matplotlib to show the statistics day by day on the screen.


• About Terms of Use:

You can change, edit, include, remove, improve, or do anything, only give the proper credits for https://github.com/licooorz87.
