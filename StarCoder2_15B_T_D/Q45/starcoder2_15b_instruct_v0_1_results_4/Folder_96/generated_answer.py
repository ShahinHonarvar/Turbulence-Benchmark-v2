def palindromes_between_indices(string):
    substring = string[3:9]
    lowercase_substring = substring.lower()
    palindromes = set()
    for i in range(len(lowercase_substring)):
        for j in range(i + 1, len(lowercase_substring) + 1):
            arrangement = lowercase_substring[i:j]
            if arrangement == arrangement[::-1]:
                palindromes.add(arrangement)
    return palindromes