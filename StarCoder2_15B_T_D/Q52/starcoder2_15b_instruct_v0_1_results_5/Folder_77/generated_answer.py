def palindrome_of_length_n(string: str) -> set:
    string = ''.join((c for c in string.lower() if c.isalpha()))
    palindromes = set()
    for i in range(0, len(string) - 173 + 1):
        substring = string[i:i + 173]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes