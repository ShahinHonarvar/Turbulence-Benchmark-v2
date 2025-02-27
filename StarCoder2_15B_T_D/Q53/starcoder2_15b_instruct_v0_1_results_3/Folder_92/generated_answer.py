def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    filtered_s = ''.join((c for c in s if c.isalpha()))
    n = 10
    result = set()
    for i in range(len(filtered_s) - n + 1):
        for j in range(i + n - 1, len(filtered_s)):
            substring = filtered_s[i:j + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result