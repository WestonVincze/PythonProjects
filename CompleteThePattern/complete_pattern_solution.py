def pattern(n):
    """Generates a multiline string pattern up to n.
    
    Args:
      n: the stopping point/number of rows for the pattern.
      
    Returns:
      A single string pattern up to 'n'.
    """
    ret = ''
    for i in range(1, n + 1):
        ret += ''.join([str(i)] * i)
        if not i == n:
            ret += '\n'
    return ret
