def palindromes_between_indices(string):
    s = string.lower()
    palindromes = set()
    for i in range(2, min(len(s), 5) + 1):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes