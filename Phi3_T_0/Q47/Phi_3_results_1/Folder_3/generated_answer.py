def palindromes_of_specific_lengths(s):
    s = s[27:96]
    palindromes = set()
    for i in range(len(s) - 4):
        for j in range(i + 49, min(i + 52, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes