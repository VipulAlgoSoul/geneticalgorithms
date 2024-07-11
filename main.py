import string
import random
from Levenshtein import distance
import numpy as np

# Optimization Algorithm Genetic
# Set a Final Value : "vipulnath"
# Create initial Samples
# Number of elements in Population: 10
# Fitness levenstien distance
# CRossover + Mutation
def create_in_element(len_trgt):
    return "".join([random.choice(string.ascii_letters) for i in range(len_trgt)])
def select_fit(target, population, pop_cnt=10):
    fitness_dict = {indv:distance(target,indv) for indv in population}
    # sorted_dict = dict(sorted(fitness_dict.items()))
    sorted_dict = sorted(fitness_dict.items(), key=lambda x: x[1])
    return [i[0] for i in sorted_dict[0:pop_cnt]], sorted_dict[0]

def gene_mutate(gene_pool,mr=0.25):
    tl = len(gene_pool)
    ml = int(tl*mr)
    random.shuffle(gene_pool)
    mutd = gene_pool[0:ml].copy()
    for i in mutd:
        mu = random.choice(string.ascii_letters)
        ind = random.choice([n for n in range(len(i))])
        mi = i.replace(i[ind], mu)
        gene_pool.append(mi)
    return gene_pool


def crossover(population, mix_num):
    pop_dict = {i:[v[0:3],v[3:6],v[6:10]] for i,v in enumerate(population)}
    new_pop = []
    gene_pool =[]
    for i in pop_dict.values():
        for k in i:
            gene_pool.append(k)
    gene_pool = gene_mutate(gene_pool)
    for num_indv in range(0,mix_num):
        ndv_ls =""
        fst = np.random.choice(gene_pool)
        ndv_ls =ndv_ls+ fst
        fst = np.random.choice(gene_pool)
        ndv_ls = ndv_ls + fst
        fst = np.random.choice(gene_pool)
        ndv_ls = ndv_ls + fst

        new_pop.append(ndv_ls)

    return new_pop

generations= 400

target = "sahadsali"
intial_population = {create_in_element(len(target)) for i in range(0,15)}
print("Initial Population", intial_population)
selected, gen_best_fitness = select_fit(target, intial_population)
print("Generation : {}, Best Individual :{}, Best Fitness Score {}"
          .format(0, gen_best_fitness[0], gen_best_fitness[1]))
for gen in range(generations):
    # do crossover

    breeded = crossover(selected,500)
    selected, gen_best_fitness = select_fit(target, breeded)
    print("Generation : {}, Best Individual :{}, Best Fitness Score {}"
          .format(gen + 1, gen_best_fitness[0], gen_best_fitness[1]))
    if gen_best_fitness[1]==0:
        break


