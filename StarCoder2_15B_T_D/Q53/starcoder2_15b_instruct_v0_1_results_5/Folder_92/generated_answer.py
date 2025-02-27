def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    s = ''.join((c for c in s if c.isalpha()))
    result = set()
    for i in range(len(s) - 9):
        for j in range(i + 10, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result