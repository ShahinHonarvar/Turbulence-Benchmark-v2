def palindrome_of_length_at_least_n(string: str) -> set:
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 3):
        for j in range(i + 4, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes