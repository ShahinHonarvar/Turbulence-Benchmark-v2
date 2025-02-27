def palindromes_of_specific_lengths(s):
    s = s[26:88].lower()
    palindromes = set()
    for i in range(len(s) - 51):
        for j in range(i + 51, min(i + 56, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes