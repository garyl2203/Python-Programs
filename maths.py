

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet
#for which a + b + c = 1000. Find the product abc.
#The answer is 31875000


def check_py_triplet(a,b,c):
    return a**2 + b**2 == c**2

def find_abc_product():
    """Returns a nested list of 3 numbers (a, b, c) that add up to 1000.
    The 3 numbers satisfy the
    constraint:  a < b < c.
    """
    total_sum = 1000
    # The maximum number that 'a' can ever be is close to 1/3 of the total sum
    max_a = total_sum/3 - 1

    for a in range(1, max_a + 1):
        b_start = a + 1
        for b in range(b_start, total_sum):
            c_start = b + 1
            for c in range(c_start, total_sum - 1):
                if a + b + c == total_sum and check_py_triplet(a,b,c):
                    return a * b * c

print find_abc_product()
