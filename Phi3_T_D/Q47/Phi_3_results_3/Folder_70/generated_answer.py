def palindromes_of_specific_lengths(s):
    s = s.lower()
    start, end = (10, min(70, len(s)))
    palindromes = set()
    for length in range(24, 53):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes