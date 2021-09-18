import random
from rsafuggvenyek import *


def pq_generalas(min=100, max=10000):
    p = random.randrange(min, max)
    while not MR_primteszt(p):
        p = random.randrange(min, max)

    q = random.randrange(min, max)
    while not MR_primteszt(q) or kibovitett_EA(p, q)[0] != 1 or p == q:
        q = random.randrange(min, max)

    return p, q


def ed_generalas(phi_n):
    e = random.randrange(2, phi_n)
    lnko, d = kibovitett_EA(e, phi_n)[:2]
    d = d % phi_n

    while lnko != 1:
        e = random.randrange(2, phi_n)
        lnko, d = kibovitett_EA(e, phi_n)[:2]
        d = d % phi_n

    return e, d


def main():
    m = int(input('Üzenet: '))
    #m = 200
    print('Eredeti üzenet:', m)

    p, q = pq_generalas()
    n = p * q
    phi_n = (p - 1) * (q - 1)

    print('p =', p)
    print('q =', q)
    print('n =', n)
    print('phi(n) =', phi_n)

    e, d = ed_generalas(phi_n)

    print('e =', e)
    print('d =', d)

    c = gyorshatvanyoz(m, e, n)

    print('c =', c)

    uzenet = kinai_maradektetel(p, q, c, d)

    print('Visszafejtett üzenet:', uzenet)


##############################################################################

if __name__ == "__main__":
    main()