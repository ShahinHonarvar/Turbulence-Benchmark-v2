def palindromes_of_specific_lengths(s):
    s = s[18:89].lower()
    palindromes = set()
    for i in range(len(s) - 11):
        for j in range(i + 12, i + 15):
            if j <= len(s):
                substring = s[i:j]
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes