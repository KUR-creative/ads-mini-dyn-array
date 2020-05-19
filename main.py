from random import randint
from dynamic_array import *
import dynamic_array as darr

#for N in range(10000, 1000000, 10000):
for N in range(10000, 100000, 1000):
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
    
    print('insert compares:', insert_comp_count, ', a time:', insert_comp_count / N,
        '| search compares:', search_comp_count, ', a time:', search_comp_count / N)
          
#dyn_arr = dynamic_array()
