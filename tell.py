import math

# x = float(input())
# floor_vai = math.floor(x)
# ceil_val = math.ceil(x)
# print(floor_vai + ceil_val)

# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())

# way = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# print(way)

# x = float(input())
# x_radians = math.radians(x)
# result = math.sin(x_radians) + math.cos(x_radians) + math.tan(x_radians) ** 2
# print(result)

# n = int(input())
# a = float(input())
# a_tall = n * a**2
# n_summ = 4 * math.tan(math.pi / n)
# result = a_tall / n_summ
# print(result)

a = float(input())
b = float(input())
arithmetic_mean = (a + b) / 2
geometric_mean = math.sqrt(a * b)
harmonic_mean = 2 * (a * b) / (a + b)
square_mean = math.sqrt((a**2 + b**2) / 2)
print(arithmetic_mean)
print(geometric_mean)
print(harmonic_mean)
print(square_mean)