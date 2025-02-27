def palindrome_of_length_n(string: str) -> set:
    string = string.lower()
    n = 420
    result = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result