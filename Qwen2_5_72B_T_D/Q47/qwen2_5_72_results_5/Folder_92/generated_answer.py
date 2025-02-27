def palindromes_of_specific_lengths(s):
    s = s[:5].lower()
    palindromes = set()
    for length in range(3, 5):
        for start in range(0, 5 - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes