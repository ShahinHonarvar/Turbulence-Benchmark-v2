def palindromes_between_indices(string):
    s = string[1:8].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 5, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes