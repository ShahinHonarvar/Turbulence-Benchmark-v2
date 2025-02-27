def palindromes_of_specific_lengths(s):
    s = s[:7].lower()
    result = set()
    for i in range(len(s)):
        for length in range(3, 7):
            if i + length <= 7:
                substr = s[i:i + length]
                if substr == substr[::-1]:
                    result.add(substr)
    return result