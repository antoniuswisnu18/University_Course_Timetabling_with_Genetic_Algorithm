from population import Population
from schedule import Schedule
import random as rnd
from display import DisplayControl


class GeneticAlgorithm:
    def __init__(self, data, en, mr, cr, ts, ps):
        self.pop_size = ps
        self.elitism_number = en
        self.mutation_rate = mr
        self.crossover_rate = cr
        self.tournament_size = ts
        self.data = data

    def develop_next_gen(self, pop):
        return self.mutation_target(self.crossover_target(pop))

    def crossover_target(self, pop):
        next_pop = Population(0, self.data)

        for i in range(0, self.elitism_number):
            next_pop.get_schedules().append(pop.get_schedules()[i])
        for i in range(self.elitism_number, self.pop_size):
            parent_1 = self.tournament(pop).get_schedules()[0]
            parent_2 = self.tournament(pop).get_schedules()[0]
            next_pop.get_schedules().append(self.crossover(parent_1, parent_2))
            i += 1
        return next_pop

    def tournament(self, pop):
        participants = Population(0, self.data)
        for i in range(self.tournament_size):
            new_candidate = pop.get_schedules()[rnd.randrange(0, self.pop_size)]
            participants.get_schedules().append(new_candidate)
        participants.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return participants

    def crossover(self, parent1, parent2):
        child = Schedule(self.data).initialize()
        for i in range(0, len(child.get_classes())):
            if rnd.random() > 0.5:
                child.get_classes()[i] = parent1.get_classes()[i]
            else:
                child.get_classes()[i] = parent2.get_classes()[i]
        return child

    def mutation_target(self, next_pop):
        for i in range(self.elitism_number, self.pop_size):
            self.mutation(next_pop.get_schedules()[i])
        return next_pop

    def mutation(self, schedule):
        new_schedule = Schedule(self.data).initialize()
        for i in range(0, len(schedule.get_classes())):
            if self.mutation_rate > rnd.random():
                schedule.get_classes()[i] = new_schedule.get_classes()[i]
        return schedule









