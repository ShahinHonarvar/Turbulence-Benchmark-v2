def palindromes_of_specific_lengths(s):
    s = s[10:101].lower()
    palindromes = set()
    for start in range(len(s) - 9):
        for end in range(start + 10, min(start + 51, len(s) + 1)):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes