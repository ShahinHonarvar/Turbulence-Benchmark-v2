def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 139):
        for j in range(i + 140, len(s) + 1):
            candidate = s[i:j]
            if candidate.isalpha() and candidate == candidate[::-1]:
                result.add(candidate)
    return result