def palindromes_of_specific_lengths(s):
    s = s[26:91].lower()
    palindromes = set()
    for start in range(len(s) - 26):
        for end in range(start + 26, min(start + 59, len(s) + 1)):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes