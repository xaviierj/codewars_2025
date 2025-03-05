'''ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.'''

def validate_pin(pin):
    # return true or false
    return len(pin) in [4, 6] and pin.isdigit() #len(pin) in [4, 6]: Checks if the length of the PIN is either 4 or 6.
                                                #pin.isdigit(): Checks if the PIN consists only of numeric characters.