def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i + 35, n + 1):
            candidate = s[i:j]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result