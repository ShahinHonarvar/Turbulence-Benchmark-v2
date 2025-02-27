def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i].lower() != s[-(i + 1)].lower():
            return False
    return True

def palindrome_of_length_at_least_n(s: str) -> set:
    s = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 14, length + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes