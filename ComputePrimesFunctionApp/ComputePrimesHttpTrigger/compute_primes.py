import sys

"""
Hopelessly inefficient way to check whether a number is prime. 
"""
def is_prime(n) :
    for i in range(2,n):
       if (n % i) == 0 :
           return False
    return True

def how_many_primes_between(m1, m2) :
    return len(list(filter(is_prime, range(m1,m2))))

def print_usage() : 
    print("")
    print("USAGE: python compute_primes.py m1 m2")
    print("")
    print("DESCRIPTION: This script will return the number of primes in the range m1:m2 (including m1, excluding m2).")
    print("")
    sys.exit(0)

if __name__ == "__main__":
    
    if len(sys.argv) != 3 :
        print_usage()
    
    m1 = int(sys.argv[1])
    m2 = int(sys.argv[2])
    if m2 <= m1 : 
        print_usage()
        raise ValueError("ERROR: m2 must be larger than m1.")
    
    print (how_many_primes_between(m1, m2))
