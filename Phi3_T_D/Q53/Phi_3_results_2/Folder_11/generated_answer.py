def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for length in range(54, len(s) - i + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                result.add(s[i:i + length])
    return result