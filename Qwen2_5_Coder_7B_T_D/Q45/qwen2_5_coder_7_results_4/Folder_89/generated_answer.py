def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = sorted(list(s))
    length = len(letters)
    if length < 6:
        return set()
    palindromes = set()
    for i in range(length):
        for j in range(i, length):
            half = ''.join(letters[i:j + 1])
            if half == half[::-1]:
                palindromes.add(half * 2)
    return palindromes