import random

POP_SIZE = 100
GENES = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'
TARGET = "Sudheer"

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calc_fitness()
        
    @classmethod
    def random_gene(cls):
        return random.choice(GENES)
        
    @classmethod
    def create_chromosome(cls):
        return [cls.random_gene() for _ in range(len(TARGET))]
        
    def mate(self, other):
        child = []
        
        for g1, g2 in zip(self.chromosome, other.chromosome):
            p = random.random()
            if p < 0.45:
                child.append(g1)
            elif p < 0.90:
                child.append(g2)
            else:
                child.append(self.random_gene())
                
        return Individual(child)
        
    def calc_fitness(self):
        return sum(1 for g, t in zip(self.chromosome, TARGET) if g != t)

def gen_population():
    return [Individual(Individual.create_chromosome()) for _ in range(POP_SIZE)]

def select_parents(pop):
    return random.sample(pop, k=2)

def crossover(p1, p2):
    child = []
    for g1, g2 in zip(p1.chromosome, p2.chromosome):
        p = random.random()
        if p < 0.45:
            child.append(g1)
        elif p < 0.90:
            child.append(g2)
        else:
            child.append(Individual.random_gene())
    return Individual(child)

def mutate(indv):
    mut_chrom = [random.choice(GENES) if random.random() < 0.1 else g for g in indv.chromosome]
    return Individual(mut_chrom)

def main():
    gen = 1
    found = False
    pop = gen_population()
    
    while not found:
        pop = sorted(pop, key=lambda x: x.fitness)
        
        if pop[0].fitness <= 0:
            found = True
            break
            
        new_gen = []
        elite_size = int(0.1 * POP_SIZE)
        new_gen.extend(pop[:elite_size])
        
        for _ in range(POP_SIZE - elite_size):
            p1, p2 = select_parents(pop)
            child = crossover(p1, p2)
            new_gen.append(child)
            
        pop = new_gen
        
        print(f"Gen: {gen}\tString: {''.join(pop[0].chromosome)}\tFitness: {pop[0].fitness}")
        gen += 1
        
    print(f"Gen: {gen}\tString: {''.join(pop[0].chromosome)}\tFitness: {pop[0].fitness}")

if __name__ == '__main__':
    main()