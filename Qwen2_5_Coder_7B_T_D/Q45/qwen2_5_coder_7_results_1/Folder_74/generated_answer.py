import itertools

def palindromes_between_indices(s):
    s = s[1:7]
    s = ''.join(filter(str.isalpha, s)).lower()
    letters = list(s)
    result = set()
    for length in range(6, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            half = ''.join(perm[:length // 2])
            if length % 2 == 0:
                if half == half[::-1]:
                    result.add(''.join(perm))
            elif half == half[::-1]:
                result.add(''.join(perm) + perm[length // 2])
    return result