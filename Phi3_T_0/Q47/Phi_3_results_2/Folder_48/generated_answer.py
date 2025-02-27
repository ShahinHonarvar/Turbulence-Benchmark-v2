def palindromes_of_specific_lengths(s):
    start, end = (155, 283)
    s = s[start - 1:end]
    palindromes = set()
    for length in range(104, 121):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes