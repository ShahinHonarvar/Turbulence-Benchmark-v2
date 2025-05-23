def palindromes_of_specific_lengths(s):
    s = s[30:85]
    palindromes = set()
    for length in range(12, 21):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes