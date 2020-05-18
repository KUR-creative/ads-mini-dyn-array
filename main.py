def is_power_of_two(n):
    return (n != 0) and (n & (n-1) == 0)

def dynamic_array():
    return []

def merge(sorted1, sorted2):
    i1,i2,idx = 0,0,0
    ret = [None] * (len(sorted1) + len(sorted2))
    while i1 + i2 < len(sorted1) + len(sorted2):
        if i1 == len(sorted1):
            ret[idx] = sorted2[i2]; i2 += 1
        elif i2 == len(sorted2):
            ret[idx] = sorted1[i1]; i1 += 1
        elif sorted1[i1] <= sorted2[i2]: # Basic Operation
            ret[idx] = sorted1[i1]; i1 += 1
        else:
            ret[idx] = sorted2[i2]; i2 += 1
        idx += 1
    return ret
    
def insert(dyn_arr, elem):
    # Find position to add elem
    pos = 0
    for idx,arr in enumerate(dyn_arr):
        if 2**idx < len(arr):
            pos = idx; break
        else: # 2**idx >= len(arr)
            pos = pos + 1

    # Merge previous elements with inserted elem
    merged = [elem]
    for idx in range(pos):
        merged = merge(merged, dyn_arr[idx])

    # Insert merged elements at pos
    dyn_arr.insert(pos, merged)
    for idx in range(pos): # Remove redundants
        del dyn_arr[0]
            
    return dyn_arr
