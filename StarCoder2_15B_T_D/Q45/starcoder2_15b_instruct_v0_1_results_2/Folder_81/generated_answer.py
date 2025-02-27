def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 2):
        for j in range(i + 3, min(len(string), i + 7) + 1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes