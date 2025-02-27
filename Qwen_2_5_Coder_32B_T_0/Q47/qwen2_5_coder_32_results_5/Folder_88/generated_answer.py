def palindromes_of_specific_lengths(s):
    s = s[11:88].lower()
    palindromes = set()
    for i in range(len(s) - 3):
        for j in range(i + 4, min(i + 6, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes