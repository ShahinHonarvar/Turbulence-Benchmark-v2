def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    n = len(s)
    palindromes = set()

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]
    for i in range(n):
        for j in range(i + 25, n + 1):
            sub = s[i:j]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub)
    return palindromes