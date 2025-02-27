def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    palindromes = set()
    for i in range(20, 22):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes