def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    result = set()
    for start in range(len(s) - 20 + 1):
        for length in [20, 21]:
            if start + length <= len(s):
                candidate = s[start:start + length]
                if candidate.isalpha() and candidate == candidate[::-1]:
                    result.add(candidate)
    return result