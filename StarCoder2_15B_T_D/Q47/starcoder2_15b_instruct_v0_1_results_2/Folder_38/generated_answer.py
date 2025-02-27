def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    for i in range(18, 88):
        for j in range(i + 38, 88):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes