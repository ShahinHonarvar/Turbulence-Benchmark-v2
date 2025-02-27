def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(3, len(string) - 1):
        for j in range(i + 1, min(i + 4, len(string))):
            if string[i] == string[j]:
                palindromes.add(string[i] + string[j])
    return palindromes