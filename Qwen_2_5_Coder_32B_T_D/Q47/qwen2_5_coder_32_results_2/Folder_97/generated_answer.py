def palindromes_of_specific_lengths(s):
    s = s[28:95].lower()
    palindromes = set()
    for start in range(len(s) - 37):
        for end in range(start + 37, min(start + 50, len(s))):
            substring = s[start:end + 1]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes