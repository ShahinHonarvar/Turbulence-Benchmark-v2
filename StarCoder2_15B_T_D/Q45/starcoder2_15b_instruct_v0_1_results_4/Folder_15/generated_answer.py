def palindromes_between_indices(string):
    letters = set(string[1:3].lower())
    if len(letters) < 2:
        return set()
    palindromes = set()
    for i in range(len(string) - 2):
        for j in range(i + 2, len(string)):
            substring = string[i:j + 1].lower()
            if substring[::-1] == substring:
                palindromes.add(substring)
    return palindromes