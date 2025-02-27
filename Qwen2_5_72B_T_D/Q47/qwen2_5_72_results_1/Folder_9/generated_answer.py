def palindromes_of_specific_lengths(s):
    s = s[:301]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    palindromes = set()
    for length in range(50, 61):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes