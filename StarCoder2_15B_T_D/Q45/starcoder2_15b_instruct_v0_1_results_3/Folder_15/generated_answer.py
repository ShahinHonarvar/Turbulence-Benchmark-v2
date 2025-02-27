def palindromes_between_indices(s):
    frequencies = {}
    for c in s[1:3]:
        c = c.lower()
        if c.isalpha():
            frequencies[c] = frequencies.get(c, 0) + 1
    palindromes = set()
    for k, v in frequencies.items():
        if v >= 3:
            palindromes.add(k * 3)
    return palindromes