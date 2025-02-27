def palindromes_of_specific_lengths(s):
    s = s[:5].lower()
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 2, min(i + 5, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes