import math


def algorithm_Sieve_prime_numbers():
    # input: an integer n > 1.
    print("Enter a number")
    num = int(input())
    # output: all prime numbers from 2 through n.
    # num = 45
   # let A be an array of Boolean values, indexed by integers 2 to n,
    # initially all set to true.
    # A = []
    # for i in range(2, num+1):
    #     A.append(True)
    #     # print(i, A)
    A = [True for i in range(num + 1)]
    # for i = 2, 3, 4, ..., not exceeding √n do
    #     if A[i] is true
    #         for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
    #             A[j] := false
    i = 2
    # for i in range(math.trunc(math.sqrt(num))):
    while (i <= math.trunc(math.sqrt(num))):
        if (A[i] == True):
            for j in range(i*2, num+1, i):
                A[j] = False

        i += 1
    A[0] = False
    A[1] = False

    # return all i such that A[i] is true.
    for i in range(num + 1):
        if A[i]:
            print(i),


algorithm_Sieve_prime_numbers()
