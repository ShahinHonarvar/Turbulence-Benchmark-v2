def palindromes_of_specific_lengths(s):
    s = s[20:75].lower()
    palindromes = set()
    for i in range(36, 43):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes