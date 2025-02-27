def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(10):
        for j in range(i + 2, 10):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                if len(substring) in range(3, 6):
                    if substring.isalpha():
                        palindromes.add(substring)
    return palindromes