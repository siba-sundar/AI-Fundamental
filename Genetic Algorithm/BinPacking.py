import random
import numpy as np

NUM_ITEMS = 20
BIN_CAPACITY = 10
ITEM_SIZES = [random.randint(1, BIN_CAPACITY//2) for _ in range(NUM_ITEMS)]

POP_SIZE = 100
MAX_GENERATIONS = 100
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
ELITE_SIZE = int(0.1 * POP_SIZE)

class Individual:
    def __init__(self, chromosome=None):
        if chromosome is None:
            self.chromosome = list(range(NUM_ITEMS))
            random.shuffle(self.chromosome)
        else:
            self.chromosome = chromosome
        
        self.normalize_bins()
        self.fitness = self.calc_fitness()
    
    def normalize_bins(self):
        bin_counts = {}
        for bin_id in self.chromosome:
            if bin_id in bin_counts:
                bin_counts[bin_id] += 1
            else:
                bin_counts[bin_id] = 1
        
        used_bins = sorted(bin_counts.keys())
        bin_mapping = {old_id: new_id for new_id, old_id in enumerate(used_bins)}
        
        self.chromosome = [bin_mapping[bin_id] for bin_id in self.chromosome]
    
    def calc_fitness(self):
        bin_loads = {}
        for item_id, bin_id in enumerate(self.chromosome):
            if bin_id in bin_loads:
                bin_loads[bin_id] += ITEM_SIZES[item_id]
            else:
                bin_loads[bin_id] = ITEM_SIZES[item_id]
        
        num_bins_used = len(bin_loads)
        
        penalty = sum(max(0, load - BIN_CAPACITY) for load in bin_loads.values())
        
        wasted_space = sum(max(0, BIN_CAPACITY - load) for load in bin_loads.values())
        
        return -(num_bins_used * 100 + wasted_space + penalty * 1000)
    
    def is_valid(self):
        bin_loads = {}
        for item_id, bin_id in enumerate(self.chromosome):
            if bin_id in bin_loads:
                bin_loads[bin_id] += ITEM_SIZES[item_id]
            else:
                bin_loads[bin_id] = ITEM_SIZES[item_id]
        
        return all(load <= BIN_CAPACITY for load in bin_loads.values())
    
    def mate(self, other):
        if random.random() < CROSSOVER_RATE:
            point1 = random.randint(0, NUM_ITEMS-2)
            point2 = random.randint(point1+1, NUM_ITEMS-1)
            
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
                chromosome[i] = random.randint(0, max(chromosome) + 1)
        return chromosome

def initialize_population():
    return [Individual() for _ in range(POP_SIZE)]

def select_parents(population):
    tournament_size = 5
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=lambda x: x.fitness)

def main():
    population = initialize_population()
    
    best_fitness = []
    
    for generation in range(MAX_GENERATIONS):
        population.sort(key=lambda x: x.fitness, reverse=True)
        
        best_fitness.append(population[0].fitness)
        
        print(f"Generation {generation}: Best fitness = {population[0].fitness}, Bins used = {max(population[0].chromosome) + 1}")
        
        if generation == MAX_GENERATIONS - 1:
            break
        
        new_population = []
        
        new_population.extend(population[:ELITE_SIZE])
        
        while len(new_population) < POP_SIZE:
            parent1 = select_parents(population)
            parent2 = select_parents(population)
            
            child1, child2 = parent1.mate(parent2)
            
            new_population.append(child1)
            if len(new_population) < POP_SIZE:
                new_population.append(child2)
        
        population = new_population
    
    best_individual = max(population, key=lambda x: x.fitness)
    print("\nFinal Solution:")
    print(f"Best packing: {best_individual.chromosome}")
    print(f"Best fitness: {best_individual.fitness}")
    
    bin_loads = {}
    for item_id, bin_id in enumerate(best_individual.chromosome):
        if bin_id in bin_loads:
            bin_loads[bin_id].append((item_id, ITEM_SIZES[item_id]))
        else:
            bin_loads[bin_id] = [(item_id, ITEM_SIZES[item_id])]
    
    print("\nBin Contents:")
    total_items_size = sum(ITEM_SIZES)
    total_bin_capacity = (max(best_individual.chromosome) + 1) * BIN_CAPACITY
    wasted_space = total_bin_capacity - total_items_size
    
    for bin_id, items in sorted(bin_loads.items()):
        bin_load = sum(size for _, size in items)
        items_str = ", ".join(f"Item {item_id}({size})" for item_id, size in items)
        print(f"Bin {bin_id}: Load = {bin_load}/{BIN_CAPACITY}, Items = {items_str}")
    
    print(f"\nTotal number of bins used: {max(best_individual.chromosome) + 1}")
    print(f"Total items size: {total_items_size}")
    print(f"Wasted space: {wasted_space}")
    print(f"Bin utilization: {total_items_size/total_bin_capacity:.2%}")

if __name__ == "__main__":
    main()