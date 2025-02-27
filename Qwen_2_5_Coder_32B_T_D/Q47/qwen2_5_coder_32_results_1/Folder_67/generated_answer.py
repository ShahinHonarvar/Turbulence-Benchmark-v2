def palindromes_of_specific_lengths(s):
    s = s[65:100].lower()
    palindromes = set()
    for i in range(len(s) - 25):
        for j in range(i + 25, min(i + 34, len(s))):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes