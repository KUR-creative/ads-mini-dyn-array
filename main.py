from random import randint

import funcy as F
from tqdm import tqdm
import matplotlib.pyplot as plt

from dynamic_array import *
import dynamic_array as darr

#for N in range(10000, 1000000, 10000):
Ns = []
insert_comp_counts = []
search_comp_counts = []
#for N in tqdm(range(10000, 100000, 1000)):
for N in tqdm(range(  1000, 400000, 1000)):
#for N in tqdm(range( 1000,  10000, 1000)):
    #N = 100000
    dyn_arr = dynamic_array()
    rand_ints = []
    for _ in range(N):
        rand_int = randint(-N,N)
        insert(dyn_arr, rand_int)

    insert_comp_count = darr.comp_count

    max_num_nts = int(N * 0.3)
    non_targets = []
    while len(non_targets) != max_num_nts:
        non_targets.append(randint(-10 * N, 10 * N))

    for num in rand_ints[: int(N * 0.7)] + non_targets:
        search(dyn_arr, num)
        
    search_comp_count = darr.comp_count - insert_comp_count
    
    #print('insert compares:', insert_comp_count, ', a time:', insert_comp_count / N,
        #'| search compares:', search_comp_count, ', a time:', search_comp_count / N)
    
    Ns.append(N)
    insert_comp_counts.append(insert_comp_count)
    search_comp_counts.append(search_comp_count)

plt.plot(Ns, insert_comp_counts, label='insert compare counts')
plt.plot(Ns, search_comp_counts, label='search compare counts')
plt.xlabel('number of items')
plt.ylabel('counts')
plt.legend()
plt.show()

insert_atimes = F.lmap(lambda count, N: count / N, insert_comp_counts, Ns)
search_atimes = F.lmap(lambda count, N: count / N, search_comp_counts, Ns)
plt.plot(Ns, insert_atimes, label='insert amortized complexity')
plt.plot(Ns, search_atimes, label='search amortized complexity')
plt.xlabel('number of items')
plt.ylabel('amortized time complexity(experimental)')
plt.legend()
plt.show()
          
#dyn_arr = dynamic_array()
