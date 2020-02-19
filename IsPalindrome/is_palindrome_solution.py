def is_palindrome(s):
    """Determines whether string passed is a palindrome.

    Args:
        s: the string to be tested.

    Returns:
        True: the passed string is a palindrome.
        False: the passed string is not a palindrome.
    """
    
    # empty dict to hold chars as keys and a count as value
    counts = {}
    # counts the number of odd letters (only 1 can exist in a palindrome)
    counter = 0

    # loop through string and either add letter to dict or increment its count by 1
    for x in s:
        if x not in counts:
            counts[x] = 1
        else:
            counts[x] += 1

    # loop through values of dict and count the odd letters
    for k, v in counts.items():
        if v % 2 != 0:
            counter += 1

    # if 2 or more counts are odd, return false: not a palindrome
    return counter <= 1
