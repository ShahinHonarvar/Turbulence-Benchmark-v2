def palindromes_of_specific_lengths(s):
    s = s[33:86].lower()
    palindromes = set()
    for i in range(len(s) - 25):
        for j in range(i + 26, i + 32):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes