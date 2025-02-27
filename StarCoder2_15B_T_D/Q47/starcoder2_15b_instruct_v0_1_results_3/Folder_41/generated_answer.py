def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(1, 8):
        for j in range(i + 2, 8):
            substring = s[i:j + 1]
            if substring.lower() == substring[::-1].lower():
                if len(substring) in range(3, 5) and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes