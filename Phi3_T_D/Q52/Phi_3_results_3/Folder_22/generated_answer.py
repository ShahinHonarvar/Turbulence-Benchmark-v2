def palindrome_of_length_n(s: str) -> {str}:
    length = 20
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes