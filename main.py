def test_horror(txt, *square, type ='мозг'):
    s = 2
    for i in square:
        s **= i
    return f'{txt} {s} {type}'
print(test_horror('Ужас в ночи', 1,2,3 ))

def fac_horror(n):
    if n == 1:
        return 1
    return fac_horror(n-1) * n
print(fac_horror(3))

