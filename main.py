#Exercise
#find duplicates of the list
s = ['a','b','c','b','n','n','m']
for i in range(len(s)):
  for j in range(i+1,len(s)):
    if s[i]==s[j]:
      print(s[i])
#andres solution

dup = []
for value in s:
  if s.count(value) >1:
    if value not in dup:
      dup.append(value)
print(dup)
