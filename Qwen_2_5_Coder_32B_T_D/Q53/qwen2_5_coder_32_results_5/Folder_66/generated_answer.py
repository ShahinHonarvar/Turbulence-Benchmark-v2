def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 76, n + 1):
            candidate = s[i:j]
            if candidate.isalpha() and candidate == candidate[::-1]:
                result.add(candidate)
    return result