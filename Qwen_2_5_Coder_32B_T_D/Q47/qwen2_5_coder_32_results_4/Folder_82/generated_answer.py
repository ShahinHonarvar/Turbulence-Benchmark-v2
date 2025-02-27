def palindromes_of_specific_lengths(s):
    s = s[3:301].lower()
    result = set()
    for start in range(29):
        for end in range(start + 29, 301):
            substr = s[start:end]
            if substr == substr[::-1]:
                result.add(substr)
    return result