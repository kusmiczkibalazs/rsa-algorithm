import random


def kibovitett_EA(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    s = 1

    while b != 0:
        r = a % b
        q = a // b

        a, b = b, r
        x, y = x1, y1

        x1 = q * x1 + x0
        y1 = q * y1 + y0

        x0, y0 = x, y

        s = -1 * s

    x = s * x0
    y = -1 * s * y0

    return a, x, y


def gyorshatvanyoz(alap, exp, mod):
    alap = alap % mod

    if exp == 0:
        return 1
    elif exp == 1:
        return alap
    elif exp % 2 == 0:
        return gyorshatvanyoz(alap * alap % mod, exp // 2, mod)
    else:
        return alap * gyorshatvanyoz(alap, exp-1, mod) % mod


def kinai_maradektetel(p, q, c, d):
    c1 = gyorshatvanyoz(c, d % (p-1), p)
    c2 = gyorshatvanyoz(c, d % (q-1), q)

    m = p * q
    m1, m2 = q, p

    y1, y2 = kibovitett_EA(q, p)[1:]

    return (c1 * y1 * m1 + c2 * y2 * m2) % m


def MR_primteszt(n, k=8):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for i in range(k):
        a = random.randrange(2, n)
        while kibovitett_EA(a, n)[0] != 1:
            a = random.randrange(2, n)

        if gyorshatvanyoz(a, d, n) == 1:
            continue

        talalt = False
        for r in range(s):
            if gyorshatvanyoz(a, d * pow(2, r), n) == n - 1:
                talalt = True
                break

        if talalt:
            continue
        else:
            return False

    return True


##############################################################################

if __name__ == "__main__":
    print(kibovitett_EA(32,45))
    print(kibovitett_EA(7,40))
    print(gyorshatvanyoz(7,180,181))
    print(gyorshatvanyoz(635,127,84))
    print(kinai_maradektetel(5,11,15,23))
    print(kinai_maradektetel(13,7,41,47))
    print(MR_primteszt(9197220353))
    print(MR_primteszt(656489800778003541130135291111884047713041254054121074264209693936416148745403190170153949))