def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    result = set()
    for i in range(len(s) - 338):
        substring = s[i:i + 338]
        if substring == substring[::-1]:
            result.add(substring)
    return result