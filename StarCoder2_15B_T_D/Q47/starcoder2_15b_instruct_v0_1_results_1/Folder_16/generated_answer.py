def palindromes_of_specific_lengths(string):
    substring = string[15:87]
    palindromes = set()
    for length in range(51, 61):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes