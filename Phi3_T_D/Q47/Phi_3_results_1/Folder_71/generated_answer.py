def palindromes_of_specific_lengths(s: str) -> set:
    s = s[17:66]
    result = set()
    for length in range(23, 37):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result