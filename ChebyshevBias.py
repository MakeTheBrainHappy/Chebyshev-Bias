"""
Chebyshev's Bias
"""

from sympy import prime #prime number sieve
import matplotlib.pyplot as plt #library for plotting 

onePrimes = 0 #4K + 1 prime count
threePrimes = 0 #4K + 3 prime count
nthPrime = 1 #specifies the nth prime number from sympy 
equalsList = [] #all instances of the nth prime where the # of 4k+1 primes = the # of 4k+3 primes
onePrimesGreaterList = [] #all instances of the nth prime where the # of 4k+1 primes > the # of 4k+3 primes
plotListPoints = [] #creates of the difference between the 4k-3 primes and the 4k-1 primes (y-axis of graph)
nthPrimeList = [] #creates a list of how many primes we have used so far (x-axis of graph)

while(nthPrime<=1000000): #check the first one million primes
    if (prime(nthPrime)%4 == 1): #checks for a 4k+1 prime
        onePrimes = onePrimes + 1 
    elif (prime(nthPrime)%4 == 3): #checks for a 4k+3 prime
        threePrimes = threePrimes + 1
    if(onePrimes == threePrimes): #checks whether the # of 4k+1 primes = the # of 4k+3 primes
        equalsList.append(nthPrime)
    elif(onePrimes > threePrimes): #checks whether the # of 4k+1 primes > the # of 4k+3 primes
        onePrimesGreaterList.append(nthPrime)
    plotListPoints.append(threePrimes-onePrimes) #adds the y-axis point
    nthPrimeList.append(nthPrime) #adds the x-axis point
    nthPrime = nthPrime+1 #moves to the next prime

plt.plot(nthPrimeList, plotListPoints, '-', color = 'r') #specifies plot features
plt.axis('tight') #specifies plot axis -> automatically generated
plt.show() #shows the plot

print("Points where the 4k+1 primes equal the 4k+3 primes:", equalsList) #all instances of the nth prime where the # of 4k+1 primes = the # of 4k+3 primes
print("Points where the 4k+1 primes are more numerous than the 4k+3 primes:", onePrimesGreaterList) #all instances of the nth prime where the # of 4k+1 primes > the # of 4k+3 primes
print("# of 4k+1 primes", onePrimes) #4K + 1 prime count
print("# of 4k+3 primes", threePrimes) #4K + 3 prime count

