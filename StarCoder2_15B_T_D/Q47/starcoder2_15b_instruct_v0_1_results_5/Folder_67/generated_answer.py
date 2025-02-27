def palindromes_of_specific_lengths(string: str) -> set:
    palindromes = set()
    for i in range(65, 100):
        for j in range(i + 26, min(i + 34, len(string))):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes