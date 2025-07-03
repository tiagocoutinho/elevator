
def solve():

  def baker(baker, floors):
    return baker != 5
  def cooper(cooper, floors):
    return cooper != 1
  def fletcher(fletcher, floors):
    cooper = floors[1]
    return fletcher > 1 and fletcher < 5 and fletcher not in (cooper - 1, cooper + 1) 
  def miller(miller, floors):
    cooper = floors[1]
    return miller > cooper
  def smith(smith, floors):
    fletcher = floors[2]
    return smith not in (fletcher - 1, fletcher + 1)

  floors = 1, 2, 3, 4, 5
  bakers = floors
  coopers = floors
  fletchers = floors
  millers = floors
  smiths = floors
  for s in smiths:
    for c in coopers:
      for b in bakers:
        for f in fletchers:
          for m in millers:
            comb = (b, c, f, m, s)
            if len(set(comb)) != 5:
                continue
            if baker(b, comb) and cooper(c, comb) and fletcher(f, comb) and miller(m, comb) and smith(s, comb):
                return comb


assert solve() == (3, 2, 4, 5, 1)