def palindromes_of_specific_lengths(s):
    s = s[18:88].lower()
    palindromes = set()
    for i in range(len(s) - 37):
        for j in range(i + 38, min(i + 61, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes