def palindromes_of_specific_lengths(s):
    s = s[39:95]
    results = set()
    for length in range(14, 53):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                results.add(substring)
    return results