import code

def all_odd_ints_exclusive(ints):
    odd_ints = []
    for i in ints:
        if i % 2 != 0:
            odd_ints.append(i)
    return odd_ints[:10]

def main():
    ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    result = all_odd_ints_exclusive(ints)
    print(result)