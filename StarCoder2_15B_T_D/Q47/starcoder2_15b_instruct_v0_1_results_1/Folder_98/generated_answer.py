def palindromes_of_specific_lengths(s):
    s_stripped = ''.join((c for c in s if c.isalpha())).lower()
    s_substr = s_stripped[:21]
    palindromes = set()
    for length in range(5, 81):
        for start in range(len(s_substr) - length + 1):
            substring = s_substr[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes