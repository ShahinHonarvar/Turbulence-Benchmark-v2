def palindromes_between_indices(string):
    palindromes = set()
    for i in range(1, len(string) - 3):
        for j in range(i + 4, len(string) + 1):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes