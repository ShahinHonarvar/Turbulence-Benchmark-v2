def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[27:78]
    for i in range(len(substring) - 18):
        for j in range(i + 18, i + 19):
            candidate = substring[i:j]
            if candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes