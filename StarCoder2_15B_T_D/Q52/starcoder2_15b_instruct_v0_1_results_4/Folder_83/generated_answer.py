def palindrome_of_length_n(string: str, n: int) -> set:
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring.isalpha() and substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes