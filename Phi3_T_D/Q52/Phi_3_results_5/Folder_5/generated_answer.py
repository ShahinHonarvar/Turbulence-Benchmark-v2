def palindrome_of_length_n(s: str) -> set:
    result = set()
    s = s.lower()
    for i in range(len(s) - 16):
        substring = s[i:i + 17]
        if substring == substring[::-1]:
            result.add(substring)
    return result