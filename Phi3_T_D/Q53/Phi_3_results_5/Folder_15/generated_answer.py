def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindrome_of_length_at_least_n(s: str) -> set:
    result = set()
    s = s.lower()
    n = len(s)
    for i in range(n):
        for j in range(i + 3, n + 1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result