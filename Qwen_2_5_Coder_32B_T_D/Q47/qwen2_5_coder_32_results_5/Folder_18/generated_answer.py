def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    palindromes = set()
    for start in range(len(s) - 12):
        for end in range(start + 13, min(start + 67, len(s) + 1)):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes