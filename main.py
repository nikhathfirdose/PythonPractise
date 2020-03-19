#pure function eample
nli =[] # since ths is outside the scope of the funcion, this will have side-effects
def mulby2(li):
  
  for item in li:
    nli.append(item*2)
  return nli
print(mulby2([1,2,3]))