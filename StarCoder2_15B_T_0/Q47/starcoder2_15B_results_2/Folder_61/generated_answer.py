def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(31):
        for j in range(i + 20, min(i + 31, len(string))):
            substring = string[i:j + 1]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes