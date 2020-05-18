from random import sample

import funcy as F
import pytest
from hypothesis import given
from hypothesis import strategies as st

from main import *

def is_sorted(lst, key=F.identity):
    return all(
        key(lst[i]) <= key(lst[i+1])
        for i in range(len(lst) - 1))
    
@given(st.iterables(st.integers()))
def test_length_of_arrays_of_dyn_arr_are_all_pow_of_2(xs):
    dyn_arr = dynamic_array()
    for x in xs:
        insert(dyn_arr, x)
        for arr in dyn_arr:
            assert is_power_of_two(len(arr))
            
@given(st.iterables(st.integers()))
def test_length_of_arrays_of_dyn_arr_are_all_different(xs):
    dyn_arr = dynamic_array()
    for x in xs:
        insert(dyn_arr, x)
        assert len(dyn_arr) == len(F.ldistinct(dyn_arr, key=len))

#@pytest.mark.skip(reason="no way of currently testing this")
@given(st.lists(st.integers()))
def test_added_elements_are_all_saved_to_dyn_arr(xs):
    dyn_arr = dynamic_array()
    for num_inseerted, x in enumerate(xs, start=1):
        insert(dyn_arr, x)
        assert len(F.lflatten(dyn_arr)) == num_inseerted
    assert set(F.flatten(dyn_arr)) == set(xs)
    
@given(st.iterables(st.integers()))
def test_arrays_of_dyn_arr_are_all_sorted_ascend(xs):
    dyn_arr = dynamic_array()
    for x in xs:
        insert(dyn_arr, x)
        for arr in dyn_arr:
            assert is_sorted(arr)
    
@given(st.iterables(st.integers()))
def test_length_of_arrays_of_dyn_arr_are_all_sorted_ascend(xs):
    dyn_arr = dynamic_array()
    for x in xs:
        insert(dyn_arr, x)
        assert is_sorted(dyn_arr, len)

#---------------------------------------------------------------
@given(st.lists(st.integers()).map(sorted),
       st.lists(st.integers()).map(sorted))
def test_merge(xs, ys):
    res = merge(xs, ys)
    assert len(res) == len(xs) + len(ys)
    # check sorted
    is_sorted(res)

@given(st.lists(st.integers(), unique_by=F.identity).map(sorted))
def test_binary_search(xs):
    targets = xs[:len(xs) // 2]
    target = sample(targets, 1)[0] if targets else None
    print('----------')
    if target and targets:
        idx = binary_search(targets, target)
        print(targets, target, idx)
        assert target == targets[idx]
    
    non_targets = xs[len(xs) // 2:]
    non_target = (sample(non_targets, 1)[0]
                  if non_targets else None)
    if non_targets:
        assert (not binary_search(targets, non_target))

@given(st.lists(st.integers(), unique_by=F.identity))
def test_search(xs):
    targets = xs[:len(xs) // 2]
    target = sample(targets, 1)[0] if targets else None
    print('----------')
    dyn_arr = dynamic_array(targets)
    if target and targets:
        pos, idx = search(dyn_arr, target)
        print(targets, target, idx)
        assert target == dyn_arr[pos][idx]
    
    non_targets = xs[len(xs) // 2:]
    non_target = (sample(non_targets, 1)[0]
                  if non_targets else None)
    if non_targets:
        assert (not search(dyn_arr, non_target))
