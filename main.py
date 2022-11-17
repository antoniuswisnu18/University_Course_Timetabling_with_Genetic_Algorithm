import sqlite3
from data_ import Data
from schedule import Schedule
from display import DisplayControl
from population import Population
from geneticalgorithm import GeneticAlgorithm

POPULATION_SIZE = 9
ELITISM_NUMBER = 1
MUTATION_RATE = 0.5
CROSSOVER_RATE = 0.5
TOURNAMENT_SIZE = 3
generation_number = 0


data = Data()
display_control = DisplayControl(data)
display_control.print_all_data()
population = Population(POPULATION_SIZE, data)
population.initialize()
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
print(f"Generation > {generation_number}")
display_control.print_population(population)
display_control.print_schedule(population.get_schedules()[0])


GA = GeneticAlgorithm(data, ELITISM_NUMBER, MUTATION_RATE, CROSSOVER_RATE, TOURNAMENT_SIZE, POPULATION_SIZE)

while population.get_schedules()[0].get_fitness() != 1.0:
    generation_number += 1
    print(f"Generation > {generation_number}")
    population = GA.develop_next_gen(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    display_control.print_population(population)
    display_control.print_schedule(population.get_schedules()[0])

print("\n\n")
