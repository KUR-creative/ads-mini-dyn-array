import funcy as F
from hypothesis import given
from hypothesis import strategies as st

from main import *

@given(st.lists(st.integers()).map(sorted))
def test_ctor(lst):
    print(lst)
    
@given(st.iterables(st.integers()))
def test_length_of_arrays_of_dyn_arr_are_all_pow_of_2(lst):
    dyn_arr = dynamic_array()
    for x in lst:
        insert(dyn_arr, x)
        for arr in dyn_arr:
            assert is_power_of_two(len(arr))
            
@given(st.iterables(st.integers()))
def test_length_of_arrays_of_dyn_arr_are_all_pow_of_2(lst):
    dyn_arr = dynamic_array()
    for x in lst:
        insert(dyn_arr, x)
        for arr in dyn_arr:
            assert is_power_of_two(len(arr))

@given(st.iterables(st.integers()))
def test_length_of_arrays_of_dyn_arr_are_all_different(lst):
    dyn_arr = dynamic_array()
    for x in lst:
        insert(dyn_arr, x)
        
        assert len(dyn_arr) == len(F.ldistinct(dyn_arr, key=len))


#def test_arrays_of_dyn_arr_are_all_sorted_itself(lst):
