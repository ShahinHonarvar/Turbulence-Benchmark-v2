def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(0, 7):
        for j in range(i + 3, min(i + 7, len(string))):
            substring = string[i:j]
            if substring == substring[::-1]:
                if all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes