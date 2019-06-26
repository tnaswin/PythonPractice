def distance_from_zero(test):
    if type(test) == int or type(test) == float:
      return abs(test)
    else:
      return "Nope"

print distance_from_zero("5")
