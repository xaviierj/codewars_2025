'''You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

a can contain numbers or strings. x can be either.

Return true if the array contains the value, false if not.'''

def check(seq, elem): # In this case, seq = array  and elem = value
    if elem in seq: 
        return True
    else:
        return False