def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(125, 284):
        for j in range(i + 109, i + 127):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes