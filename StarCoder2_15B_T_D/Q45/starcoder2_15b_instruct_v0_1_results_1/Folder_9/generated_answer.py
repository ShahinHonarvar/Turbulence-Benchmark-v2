def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 6):
        for j in range(i + 6, len(string)):
            if string[i:j + 1] == string[i:j + 1][::-1]:
                palindromes.add(string[i:j + 1])
    return palindromes