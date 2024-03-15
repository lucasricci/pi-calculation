# https://en.wikipedia.org/wiki/Chudnovsky_algorithm#Optimizations

from decimal import Decimal, getcontext

getcontext().prec = 1000


def factorial(n):
    if n == 0 or n == 1:
        return Decimal(1)
    else:
        result = Decimal(1)
        for i in range(2, n + 1):
            result *= Decimal(i)
        return result


def chudnovsky(n):
    pi = Decimal(0)

    for k in range(n):
        top = ((-1) ** k) * (factorial(6 * k)) * (545140134 * k + 13591409)
        den = (
            (factorial(3 * k)) * ((factorial(k)) ** 3) * ((640320) ** (3 * k))
        )
        pi += Decimal(top) / Decimal(den)
        print(k, flush=False)

    pi *= Decimal(1) / (Decimal(426880) * Decimal(10005).sqrt())
    return 1 / pi


if __name__ == "__main__":
    iterations = int(
        input("How many iterations you want the algorithm to compute? ")
    )
    print(chudnovsky(iterations))
