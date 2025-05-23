def palindromes_of_specific_lengths(s):
    s = s[44:100].lower()
    palindromes = set()
    for i in range(len(s) - 12):
        for j in range(i + 13, min(i + 43, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes