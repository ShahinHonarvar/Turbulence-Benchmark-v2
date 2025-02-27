def palindromes_of_specific_lengths(string):
    palindromes = set()
    length_range = range(40, 73)
    for i in range(15, 90):
        for j in range(i + min(length_range), i + max(length_range) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                if all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes