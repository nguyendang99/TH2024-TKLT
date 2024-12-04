print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
def sieve_of_eratosthenes(limit):
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False
    return [num for num, prime in enumerate(is_prime) if prime]
limit = 10**6
P = tuple(sieve_of_eratosthenes(limit))
print("Tuple P gồm các số nguyên tố nhỏ hơn 1 triệu:")
print(P)
