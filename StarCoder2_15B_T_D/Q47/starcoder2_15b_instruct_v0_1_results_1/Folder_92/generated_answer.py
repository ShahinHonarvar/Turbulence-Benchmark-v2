def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(len(string) - 4):
        for j in range(i + 3, i + 5):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes