def palindromes_of_specific_lengths(s):
    s = s[11:88]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    lengths = range(4, 6)
    for length in lengths:
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return set((p.upper() for p in palindromes))