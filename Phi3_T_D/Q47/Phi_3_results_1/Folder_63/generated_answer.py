def palindromes_of_specific_lengths(s):
    start = 33
    end = 85
    s = s.lower()
    palindromes = set()
    for length in range(26, 32):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes