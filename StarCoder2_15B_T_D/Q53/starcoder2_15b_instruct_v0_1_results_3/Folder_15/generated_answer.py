def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 4, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result