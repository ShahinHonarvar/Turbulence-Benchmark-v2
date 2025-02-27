def palindromes_between_indices(s):
    s = s[1:10].lower()
    letters = set(s)
    result = set()
    for i in range(len(letters), 6, -1):
        for perm in itertools.permutations(letters, i):
            half = ''.join(perm[:i // 2])
            if half == half[::-1]:
                result.add(''.join(perm) + half[::-1])
    return result