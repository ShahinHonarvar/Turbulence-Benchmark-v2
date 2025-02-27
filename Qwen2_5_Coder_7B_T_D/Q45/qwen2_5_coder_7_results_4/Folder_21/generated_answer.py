def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 7, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes