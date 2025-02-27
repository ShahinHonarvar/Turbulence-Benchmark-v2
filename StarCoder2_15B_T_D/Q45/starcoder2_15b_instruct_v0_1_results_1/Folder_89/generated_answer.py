def palindromes_between_indices(string):
    substring = string[5:10].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring) + 1):
            arrangement = substring[i:j]
            if arrangement == arrangement[::-1] and len(arrangement) >= 6:
                palindromes.add(arrangement)
    return palindromes