def pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

print (pythagorean_triple(3, 4, 5))
print (pythagorean_triple(3, 9, 15))