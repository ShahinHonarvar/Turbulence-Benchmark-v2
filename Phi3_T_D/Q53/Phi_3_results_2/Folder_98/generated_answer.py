def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s)):
        for length in range(6, len(s) - i + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result