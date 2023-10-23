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

def crossover(population, mix_num):
    pop_dict = {i:[v[0:3],v[3:6],v[6:10]] for i,v in enumerate(population)}
    # print(pop_dict)
    new_pop = []
    for num_indv in range(0,mix_num):
        ndv_ls =""
        fst = np.random.choice(list(pop_dict.keys()))
        fst_i = np.random.choice([0,1,2])
        print(fst, fst_i, pop_dict.keys())

        ndv_ls =ndv_ls+ pop_dict[fst][fst_i]
        print(ndv_ls)
        fst = np.random.choice(list(pop_dict.keys()))
        fst_i = np.random.choice([0, 1, 2])
        ndv_ls = ndv_ls + pop_dict[fst][fst_i]
        print(ndv_ls)
        fst = np.random.choice(list(pop_dict.keys()))
        fst_i = np.random.choice([0, 1, 2])
        ndv_ls = ndv_ls + pop_dict[fst][fst_i]
        print(ndv_ls)
        new_pop.append(ndv_ls)
        print(ndv_ls)
    return new_pop

generations= 4

target = "vipulnath"
intial_population = {create_in_element(len(target)) for i in range(0,15)}
selected, gen_best_fitness = select_fit(target, intial_population)
print("Generation : {}, Best Individual :{}, Best Fitness Score {}"
          .format(0, gen_best_fitness[0], gen_best_fitness[1]))
for gen in range(generations):
    # do crossover

    breeded = crossover(selected,50)
    selected, gen_best_fitness = select_fit(target, breeded)
    print("Generation : {}, Best Individual :{}, Best Fitness Score {}"
          .format(gen + 1, gen_best_fitness[0], gen_best_fitness[1]))

