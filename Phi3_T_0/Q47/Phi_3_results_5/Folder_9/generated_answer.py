def palindromes_of_specific_lengths(s):
    s = s[:301].lower()
    palindromes = set()
    for i in range(50, 61):
        for j in range(301 - i + 1):
            substring = s[j:j + i]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes