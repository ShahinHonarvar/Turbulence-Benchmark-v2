def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[130:296]
    for i in range(len(substring) - 103):
        for j in range(103, 159):
            if i + j <= len(substring):
                candidate = substring[i:i + j]
                if candidate.lower() == candidate[::-1].lower():
                    palindromes.add(candidate)
    return palindromes