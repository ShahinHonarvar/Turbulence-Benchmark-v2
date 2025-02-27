def palindromes_of_specific_lengths(s):
    s = s[30:96].lower()
    palindromes = set()
    for start in range(len(s) - 33):
        for end in range(start + 33, min(start + 55, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes