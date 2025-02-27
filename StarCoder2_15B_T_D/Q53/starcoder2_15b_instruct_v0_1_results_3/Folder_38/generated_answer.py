def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindrome_of_length_at_least_n(s: str, n: int) -> set:
    s_lower = s.lower()
    s_filtered = ''.join((c for c in s_lower if c.isalpha()))
    result = set()
    for i in range(len(s_filtered) - n + 1):
        for j in range(i + n, len(s_filtered) + 1):
            substring = s_filtered[i:j]
            if is_palindrome(substring):
                result.add(substring)
    return result