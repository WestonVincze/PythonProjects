def tickets(people):
  """Determines whether it is possible for clerk to sell tickets to every person in line.
  
  Args:
    people: array that represents people in line and the size of dollar bill they have.
    
  Returns:
    'YES': the clerk will be able to provide change.
    'NO': the clerk will not have enough money to give change.
  """
  
  # create a 'till' to store bills
  till = { 25 : 0,
           50 : 0,
           100 : 0, }
  
  for order in people:
    # 25 means no change is needed, add to till
    if order == 25: 
      till[25] += 1
    # only add to till if at least one 25 bill is available
    elif order == 50 and till[25] >= 1:
      till[50] += 1
      till[25] -= 1
    # add to till if a 50 and a 25 bill are available
    elif order == 100 and till[50] >= 1 and till[25] >= 1:
      till[100] += 1
      till[50] -= 1
      till[25] -= 1
    # or add to till if 3 25 bills are available
    elif order == 100 and till[25] >= 3:
      till[100] += 1
      till[25] -= 3
    # improper change causes fail, return NO
    else:
      return "NO"
      
  # no news is good news, return Yes.
  return "YES"
