def palindromes_between_indices(string):
    string = ''.join([c for c in string.lower() if c.isalpha()])
    palindromes = set()
    for i in range(4, len(string) - 2):
        substring = string[i:i + 3]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes