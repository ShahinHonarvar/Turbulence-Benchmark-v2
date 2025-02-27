def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(23, 40):
        for start in range(31, 75):
            end = start + length - 1
            if end > 74:
                break
            substring = s[start:end + 1].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result