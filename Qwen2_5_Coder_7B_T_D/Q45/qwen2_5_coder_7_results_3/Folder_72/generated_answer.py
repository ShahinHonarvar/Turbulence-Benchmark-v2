def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    letters = set(s[1:8].lower())
    even_len = set()
    odd_len = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(i, j + 1):
                if k == i or k == j:
                    odd_len.add(letters[k])
                else:
                    even_len.add(letters[k])
    palindromes = set()
    for e in even_len:
        for o in odd_len:
            for i in range(3):
                p = e * i + o + e[::-1] * i
                if len(p) >= 6:
                    palindromes.add(p)
            for i in range(3):
                p = e[::-1] * i + o + e * i
                if len(p) >= 6:
                    palindromes.add(p)
    return palindromes