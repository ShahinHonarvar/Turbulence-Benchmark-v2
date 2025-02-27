def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(62, 89):
        for j in range(i + 18, i + 22):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes