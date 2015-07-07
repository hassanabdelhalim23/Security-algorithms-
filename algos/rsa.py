from fractions import  gcd
import random

def mod_inverse(divisor, dividend):
        al_temp = dividend
        A = [divisor, dividend]
        Q = [0]
        X = []
        i = 1
        while al_temp != 0:
            Q.insert(i, A[i - 1] / A[i])
            A.insert(i + 1, A[i - 1] % A[i])
            al_temp = A[i + 1]
            i += 1

        x_length = len(Q)
        i = 0
        while i < x_length:
            if i != x_length - 2:
                X.insert(i, 0)
            else:
                X.insert(i, 1)
            i += 1

        x_length -= 3
        while x_length >= 0:
            new_x = Q[x_length + 1] * X[x_length + 1] + X[x_length + 2]
            X[x_length] = new_x
            x_length -= 1

        checker = A[0] * X[1] - A[1] * X[0]
        #print A[0], X[1], A[1], X[0]
        #print "checker: ", checker
        if checker == -1:
            return X[0]
        else:
            return -1 * X[0] % dividend


def repeated_squaring(base, power, mod):
    result = 1
    power_binary = power_to_bin(power)
    for i in power_binary:
        if i == 1:
            result = (result * base) % mod
        base = base * base % mod
    return result


def power_to_bin(power):
    _list = []
    while power != 0:
        _list.append(power % 2)
        power //= 2
    return _list

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    else:
        for div in range(2,num):
            if num % div == 0:
                return False
        return True

def encrypt(p, q, message):
    if is_prime(p) != True or is_prime(q) != True:
        return "p and q must be primes"
    # p = random.randrange(2, 20, 1)
    # if p % 2 == 0:
    #     p += 1
    # q = random.randrange(2, 20, 1)
    # if q % 2 == 0:
    #     q += 1
    # while is_prime(p) != True:
    #     p += 2
    # while is_prime(q) != True and p != q:
    #     q += 2

    # print p, q
    n = p * q
    z = (p - 1) * (q - 1)
    e = 1
    for i in range(2, n):
        if gcd(i, z) == 1:
            e = i
            break
    d = mod_inverse(z, e)
    # print "e: ", e," ,d: ", d
    if d == e:
        d += z
    output = []
    for char in message:
        output.append(chr(repeated_squaring(ord(char) - 97, e, n) + 97))
    #print output
    return ''.join(output)

def decrypt(p, q, message):
    if is_prime(p) != True or is_prime(q) != True:
        return "p and q must be primes"
    # p = random.randrange(2,100, 1)
    # if p % 2 == 0:
    # 	p += 1
    # q = random.randrange(2,100, 1)
    # if q % 2 == 0:
    # 	q += 1
    # while is_prime(p) != True:
    # 	p += 2
    # while is_prime(q) != True:
    # 	q += 2

    n = p * q
    z = (p - 1) * (q - 1)
    e = 1
    for i in range(2, n):
        if gcd(i, z) == 1:
            e = i
            break
    d = mod_inverse(z, e)
    if d == e:
        d += z
    output = []
    for char in message:
        output.append(chr(repeated_squaring(ord(char) - 97, d, n) + 97))
    return ''.join(output)

# print encrypt(5, 7, "mpx")
# print decrypt(5, 7, "rps")