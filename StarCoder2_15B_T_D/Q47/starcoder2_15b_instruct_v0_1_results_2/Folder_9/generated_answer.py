def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(301):
        for j in range(i + 50, i + 61):
            substring = string[i:j]
            if substring == substring[::-1]:
                if all((ch.isalpha() for ch in substring)):
                    palindromes.add(substring)
    return palindromes