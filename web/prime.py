# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Loop through numbers from 1 to 100 and print primes
for num in range(1, 101):
    if is_prime(num):
        print(num)