import time
import math
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)
star_time = time.time(       )
n = 3
resultado = fatorial(n)
print(resultado)

#usando o for

