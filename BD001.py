list = [1,5,8,66,3,9,5,25,5,38,20]       # find third max
max=second_max=third_max =list[0]
for i in list:
  if i > max:
    third_max = second_max
    second_max = max
    max = i
  elif i > second_max:
    third_max = second_max
    second_max = i
  elif i > third_max:
    third_max = i

print("first_max:", max)
print("second_max:" ,second_max)
print("third_max:" ,third_max)