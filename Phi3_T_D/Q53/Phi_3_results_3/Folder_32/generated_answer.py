def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for length in range(70, len(s) - i + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result