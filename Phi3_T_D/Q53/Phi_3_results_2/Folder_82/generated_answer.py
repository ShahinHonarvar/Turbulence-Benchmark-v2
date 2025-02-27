def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 65, len(s)):
            substr = s[i:j + 1]
            if len(substr) >= 72 and substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result