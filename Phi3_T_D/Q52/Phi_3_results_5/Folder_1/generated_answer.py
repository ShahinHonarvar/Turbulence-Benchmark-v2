def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n - 26):
        substring = s[i:i + 27]
        if substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes