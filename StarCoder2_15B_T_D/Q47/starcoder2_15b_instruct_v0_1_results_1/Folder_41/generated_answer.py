def palindromes_of_specific_lengths(string):
    substring = string[1:8]
    palindromes = set()
    for i in range(len(substring) - 2):
        for j in range(i + 3, min(i + 5, len(substring) + 1)):
            if substring[i:j] == substring[i:j][::-1]:
                if all((c.isalpha() for c in substring[i:j])):
                    palindromes.add(substring[i:j])
    return palindromes