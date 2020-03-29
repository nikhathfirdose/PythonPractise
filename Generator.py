#exampele for generatos
def fun(iterable):
  iterator= iter(iterable)
  while True:
    try:
      print(iterator)
      print(next(iterator))
      # next(iterator) #everything stored at same location, hence increases efficiency
      
    except StopIteration:
        break
fun([1,2,4])