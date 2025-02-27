def palindrome_of_length_at_least_n(s: str) -> set:
    processed_string = ''.join((c for c in s.lower() if c.isalpha()))
    result = set()
    for i in range(len(processed_string) - 84 + 1):
        substring = processed_string[i:i + 84]
        if substring == substring[::-1]:
            result.add(substring)
    return result