def factory(n):
    return lambda a : a * n

double = factory(2)
triple = factory(3)

print(double(10))
# 20

print(triple(10))
# 30