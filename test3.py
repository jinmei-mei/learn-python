def factortial(n):
    if n ==0:
        return 1
    return n * factortial(n-1)


d = factortial(4)
print(d)