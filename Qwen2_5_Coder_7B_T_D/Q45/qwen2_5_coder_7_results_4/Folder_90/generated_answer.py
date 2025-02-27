def palindromes_between_indices(s):
    s = s[0:6].lower()
    letters = set(s)
    palindromes = set()
    for length in range(4, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes