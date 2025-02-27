def palindrome_of_length_n(s: str) -> set:
    s = ''.join((c for c in s.lower() if c.isalpha()))
    result = set()
    for i in range(len(s) - 88 + 1):
        substring = s[i:i + 88]
        if substring == substring[::-1]:
            result.add(substring)
    return result