def palindromes_of_specific_lengths(s):
    results = set()
    for length in range(154, 183):
        for start in range(101, 293 - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                results.add(substring.lower())
    return results