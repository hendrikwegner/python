import random
import sys

#length = int(input('Wie groß soll das Array sein?:'))
length = int(sys.argv[1])
list = random.sample(range(1, length+1), length)

def sort(list):
  for i in range(0, len(list)-1):
    if(list[i] > list[i+1]):
      swap(i, i+1)


def swap(x, y):
  temp = list[y]
  list[y] = list[x]
  list[x] = temp

for i in range (0, len(list)):
  print(list)
  sort(list)
