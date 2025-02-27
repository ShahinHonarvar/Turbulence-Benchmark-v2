def palindromes_between_indices(string):
    palindromes = set()
    for i in range(6, len(string) - 1):
        for j in range(i + 1, min(i + 4, len(string))):
            for k in range(j + 1, len(string)):
                substring = string[i:k + 1]
                if substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes