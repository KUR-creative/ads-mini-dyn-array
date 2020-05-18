def is_power_of_two(n):
    return (n != 0) and (n & (n-1) == 0)

def dynamic_array():
    return []

def insert(dyn_arr, elem):
    dyn_arr.append((elem,))
