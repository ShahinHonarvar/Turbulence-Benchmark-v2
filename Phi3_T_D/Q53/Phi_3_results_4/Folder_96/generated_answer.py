def palindrome_of_length_at_least_n(s: str, n: int=24) -> set:

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if all((c.isalpha() for c in substring)) and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes