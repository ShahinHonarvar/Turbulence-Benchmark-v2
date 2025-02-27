def palindromes_of_specific_lengths(s):
    s = s[:21]
    s_lower = s.lower()
    palindromes = set()
    for length in range(5, 81):
        for start in range(0, 21 - length + 1):
            substring = s_lower[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes