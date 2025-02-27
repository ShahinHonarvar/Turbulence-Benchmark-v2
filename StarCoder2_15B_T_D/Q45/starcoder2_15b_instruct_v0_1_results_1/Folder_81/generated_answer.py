def palindromes_between_indices(s: str) -> set:

    def is_palindrome(s: str) -> bool:
        return s.lower() == s.lower()[::-1]

    def get_palindromes(s: str, current: str, start: int, end: int) -> None:
        if len(current) >= 3 and is_palindrome(current):
            result.add(current)
        if start > end:
            return
        for i in range(start, end + 1):
            get_palindromes(s, current + s[i], i + 1, end)
    result = set()
    get_palindromes(s, '', 0, 6)
    return result