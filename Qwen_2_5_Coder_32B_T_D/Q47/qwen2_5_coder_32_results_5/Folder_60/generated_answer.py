def palindromes_of_specific_lengths(s):
    s = s[23:83].lower()
    palindromes = set()
    for i in range(len(s) - 31):
        for j in range(i + 32, min(i + 35, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes