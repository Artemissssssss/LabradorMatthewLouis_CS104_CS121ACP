def print_multiples_of_7(limit):
    for i in range(1, limit + 1):
        print(f"\t{i * 7}" if i % 2 == 0 else i * 7)

print_multiples_of_7(10)
