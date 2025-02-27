def palindromes_between_indices(string):
    substring = string[5:10].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            for k in range(j + 1, len(substring)):
                for l in range(k + 1, len(substring)):
                    permutation = substring[i] + substring[j] + substring[k] + substring[l]
                    if permutation == permutation[::-1]:
                        palindromes.add(permutation)
    return palindromes