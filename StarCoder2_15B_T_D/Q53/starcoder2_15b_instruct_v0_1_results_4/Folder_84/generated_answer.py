def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 80):
        for j in range(i + 80, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes