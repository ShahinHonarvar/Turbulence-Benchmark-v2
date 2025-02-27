def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 144 + 1):
        for j in range(i + 144, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes