import functools

def add_letters(*letters):
    """Summation of letters into one letter if each letter is given value from 
    1 through 26 and values higher than 26 continue from 1. 

    Args:
        *letters: various letters to be added up. 

    Returns:
        Single character that represents the "summation" of the passed letters.

    Example:
        add_letters('a', 'b', 'c') returns 'f'
    """
    # if no letters, return z
    if len(letters) == 0:
        return "z"
    
    # alphabet from 97 - 122 in ascii
    # convert alphabet into values from 1 to 26
    values = [ord(l) - 96 for l in letters]
    
    # add up the total values
    total = functools.reduce(lambda x,y: x + y, values)
    
    # if there is overflow, determine value 
    if total > 26:
        # if the total is perfectly divisible by 26, resulting in 0
        # manually set total to 26
        total = total % 26 if total % 26 != 0 else 26

    # convert total into ascii character (adding the 96 we took earlier)
    return chr(total + 96)
