def palindrome_of_length_at_least_n(s):
    n = 42
    s = s.lower()
    results = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if len(substr) >= n and substr == substr[::-1] and substr.isalpha():
                results.add(substr)
    return results