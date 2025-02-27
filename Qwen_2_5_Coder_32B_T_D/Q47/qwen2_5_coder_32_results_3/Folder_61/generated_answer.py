def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    palindromes = set()
    for start in range(31):
        for end in range(start + 19, 31):
            substring = s[start:end + 1]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes