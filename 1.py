
def sum_1_to_n(n):
    if n < 0:
        raise 'n must be positive'
    else:
        return int(n * (n + 1) / 2)

print(sum_1_to_n(1))
print(sum_1_to_n(3))
print(sum_1_to_n(10))
