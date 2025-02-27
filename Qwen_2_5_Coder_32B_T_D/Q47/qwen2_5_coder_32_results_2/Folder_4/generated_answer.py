def palindromes_of_specific_lengths(s):
    s = s[12:93].lower()
    palindromes = set()
    for start in range(len(s) - 16):
        for end in range(start + 17, min(start + 67, len(s) + 1)):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes