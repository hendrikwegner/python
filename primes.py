import sys
import math
import time


def is_prime(number):
    prime = True
    limit = int(math.sqrt(number) + 1)
    for i in range(2, limit):
        if number % i == 0:
            prime = False
    return prime


start = time.time()

primes = []
j = 0
while len(primes) < int(sys.argv[1]):
    if is_prime(j):
        #print(j, end=", ")
        primes.append(j)
    j = j + 1

ende = time.time()
print(primes)
print('Gesamtzeit: {:6.3f}s and {} iterrations'.format(ende - start, j))

startSum = time.time()
sum = 0
for i in range(0, len(primes)):
    sum = sum + primes[i]
average = sum / len(primes)
endSum = time.time()
print('Gesamtzeit (Schnitt): {:6.3f}s Schnitt: {}'.format(endSum - startSum, average))
