def palindromes_of_specific_lengths(s):
    s = s[11:94].lower()
    palindromes = set()
    for i in range(len(s) - 33):
        for j in range(i + 33, min(i + 55, len(s))):
            substring = s[i:j + 1]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes