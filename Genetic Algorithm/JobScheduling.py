import random
import numpy as np

NUM_JOBS = 10
NUM_MACHINES = 3
PROCESSING_TIMES = [random.randint(1, 10) for _ in range(NUM_JOBS)]

POP_SIZE = 100
MAX_GENERATIONS = 100
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
ELITE_SIZE = int(0.1 * POP_SIZE)

class Individual:
    def __init__(self, chromosome=None):
        if chromosome is None:
            self.chromosome = [random.randint(0, NUM_MACHINES-1) for _ in range(NUM_JOBS)]
        else:
            self.chromosome = chromosome
        self.fitness = self.calc_fitness()
    
    def calc_fitness(self):
        machine_times = [0] * NUM_MACHINES
        
        for job_id, machine_id in enumerate(self.chromosome):
            machine_times[machine_id] += PROCESSING_TIMES[job_id]
        
        max_completion_time = max(machine_times)
        
        return -max_completion_time
    
    def mate(self, other):
        if random.random() < CROSSOVER_RATE:
            point1 = random.randint(0, NUM_JOBS-2)
            point2 = random.randint(point1+1, NUM_JOBS-1)
            
            child1_chromosome = self.chromosome[:point1] + other.chromosome[point1:point2] + self.chromosome[point2:]
            child2_chromosome = other.chromosome[:point1] + self.chromosome[point1:point2] + other.chromosome[point2:]
            
            child1_chromosome = self.mutate(child1_chromosome)
            child2_chromosome = self.mutate(child2_chromosome)
            
            return Individual(child1_chromosome), Individual(child2_chromosome)
        else:
            return Individual(self.chromosome[:]), Individual(other.chromosome[:])
    
    def mutate(self, chromosome):
        for i in range(len(chromosome)):
            if random.random() < MUTATION_RATE:
                chromosome[i] = random.randint(0, NUM_MACHINES-1)
        return chromosome

def initialize_population():
    return [Individual() for _ in range(POP_SIZE)]

def select_parents(population):
    fitness_values = [ind.fitness - min(ind.fitness for ind in population) + 1 for ind in population]
    total_fitness = sum(fitness_values)
    
    selection_probs = [f/total_fitness for f in fitness_values]
    
    parents = random.choices(population, weights=selection_probs, k=2)
    return parents[0], parents[1]

def main():
    population = initialize_population()
    
    best_fitness = []
    
    for generation in range(MAX_GENERATIONS):
        population.sort(key=lambda x: x.fitness, reverse=True)
        
        best_fitness.append(population[0].fitness)
        
        print(f"Generation {generation}: Best fitness = {population[0].fitness}, Best schedule = {population[0].chromosome}")
        
        if generation == MAX_GENERATIONS - 1:
            break
        
        new_population = []
        
        new_population.extend(population[:ELITE_SIZE])
        
        while len(new_population) < POP_SIZE:
            parent1, parent2 = select_parents(population)
            
            child1, child2 = parent1.mate(parent2)
            
            new_population.append(child1)
            if len(new_population) < POP_SIZE:
                new_population.append(child2)
        
        population = new_population
    
    best_individual = max(population, key=lambda x: x.fitness)
    print("\nFinal Solution:")
    print(f"Best schedule: {best_individual.chromosome}")
    print(f"Best fitness: {best_individual.fitness}")
    
    machine_loads = [0] * NUM_MACHINES
    for job_id, machine_id in enumerate(best_individual.chromosome):
        machine_loads[machine_id] += PROCESSING_TIMES[job_id]
    
    print(f"Processing times: {PROCESSING_TIMES}")
    print(f"Machine loads: {machine_loads}")
    print(f"Makespan (total completion time): {max(machine_loads)}")

if __name__ == "__main__":
    main()