import random

CAP = 60
WTS = [12, 22, 32, 42, 52]
VALS = [70, 110, 130, 160, 210]
POP_SIZE = 40
GENS = 80
MUT_RATE = 0.08

def make_chromo():
    return [random.choice([0, 1]) for _ in range(len(WTS))]

def init_pop():
    return [make_chromo() for _ in range(POP_SIZE)]

def calc_fit(chromo):
    w = sum(w * g for w, g in zip(WTS, chromo))
    v = sum(v * g for v, g in zip(VALS, chromo))
    return v if w <= CAP else -1

def select_parents(pop):
    fits = [calc_fit(ch) for ch in pop]
    min_fit = min(fits)
    if min_fit < 0:
        fits = [f - min_fit for f in fits]
    total_fit = sum(fits)
    probs = [f / total_fit for f in fits]
    return [pop[i] for i in random.choices(range(len(pop)), probs, k=POP_SIZE)]

def crossover(p1, p2):
    pt1, pt2 = sorted(random.sample(range(len(p1)), 2))
    return (p1[:pt1] + p2[pt1:pt2] + p1[pt2:], p2[:pt1] + p1[pt1:pt2] + p2[pt2:])

def mutate(chromo):
    if random.random() < MUT_RATE:
        idx = random.randint(0, len(chromo) - 1)
        chromo[idx] ^= 1

def genetic_algo():
    pop = init_pop()
    for _ in range(GENS):
        parents = select_parents(pop)
        offspr = []
        for i in range(0, len(parents) - 1, 2):
            offspr.extend(crossover(parents[i], parents[i + 1]))
        for ch in offspr:
            mutate(ch)
        pop = offspr
    best = max(pop, key=calc_fit)
    return best, calc_fit(best)

best_sol, best_val = genetic_algo()
print("Best Solution (Selected items):", best_sol)
print("Best Fitness (Total value):", best_val)
