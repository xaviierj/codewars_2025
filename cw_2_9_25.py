'''Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.'''

def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0')) # rstrip() removes any character but needs to be converted into a str first
    except ValueError:
        return 0


no_boring_zeros(0)