def palindromes_of_specific_lengths(s: str) -> set:
    result = set()
    s = s[75:96].lower()
    for length in range(7, 10):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result