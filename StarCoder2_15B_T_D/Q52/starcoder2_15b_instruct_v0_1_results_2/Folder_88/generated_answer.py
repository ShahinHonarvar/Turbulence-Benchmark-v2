def palindrome_of_length_n(s: str) -> set:
    palindromes = set()
    n = 13
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes