def palindromes_between_indices(string):
    palindromes = set()
    for i in range(2, len(string) - 1):
        for j in range(i + 7, len(string)):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes