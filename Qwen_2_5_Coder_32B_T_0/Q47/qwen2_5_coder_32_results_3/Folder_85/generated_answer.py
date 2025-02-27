def palindromes_of_specific_lengths(s):
    s = s[29:99].lower()
    palindromes = set()
    for i in range(len(s) - 5):
        for j in range(i + 6, min(i + 10, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes