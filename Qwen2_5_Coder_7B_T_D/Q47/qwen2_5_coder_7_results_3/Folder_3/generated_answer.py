def palindromes_of_specific_lengths(s):
    s = s[27:96].lower()
    result = set()
    for start in range(len(s) - 50):
        for length in [49, 50, 51]:
            end = start + length
            if end > len(s):
                break
            substring = s[start:end]
            if substring == substring[::-1]:
                result.add(substring)
    return result