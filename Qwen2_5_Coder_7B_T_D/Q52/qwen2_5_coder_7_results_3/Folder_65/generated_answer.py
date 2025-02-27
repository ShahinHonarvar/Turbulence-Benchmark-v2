def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    result = set()
    for i in range(len(s) - 34):
        substring = s[i:i + 35]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result