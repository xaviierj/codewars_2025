'''You are given two sorted arrays that contain only integers. 

These arrays may be sorted in either ascending or descending order. Your task is to merge them into a single array, ensuring that:

The resulting array is sorted in ascending order.

Any duplicate values are removed, so each integer appears only once.

If both input arrays are empty, return an empty array.

No input validation is needed, as both arrays are guaranteed to contain zero or more integers.'''


'My solution'

def merge_arrays(arr1, arr2):
    merged = arr1 + arr2
    new_array = list(set(merged)) # set() function automatically removes duplicates 
    new_array.sort()
    return new_array
    
'Alt Solutions'

def merge_arrays(arr1, arr2):
    return sorted(set(arr1+arr2))

def merge_arrays(arr1, arr2):
    return sorted(list(set(arr1 + arr2)))