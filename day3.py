"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

pfact = 0
i=1
num = 600851475143

while i <= num:
    if (num%i==0):
        pfact = i
        num/=i
        i+=1
    i+=1
print(pfact)