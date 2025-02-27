def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    n = 59
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes