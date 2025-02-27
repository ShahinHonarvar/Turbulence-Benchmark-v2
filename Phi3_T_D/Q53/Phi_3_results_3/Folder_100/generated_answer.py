def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindrome_of_length_at_least_n(text: str) -> set:
    text = text.lower()
    palindromes = set()
    size = 48
    while size <= len(text):
        for i in range(len(text) - size + 1):
            substring = text[i:i + size]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
        size += 1
    return palindromes