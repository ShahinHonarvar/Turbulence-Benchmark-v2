def palindrome_of_length_at_least_n(s: str) -> set:

    def is_palindrome(s: str) -> bool:
        return len(s) >= 36 and s.lower() == s[::-1].lower()
    palindromes = set()
    for i in range(len(s) - 35):
        substring = s[i:i + 36]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes