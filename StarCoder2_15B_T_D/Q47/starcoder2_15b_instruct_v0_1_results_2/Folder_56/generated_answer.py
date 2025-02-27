def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(1, 10):
        for j in range(i + 2, min(i + 8, len(s))):
            substring = s[i:j + 1]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes