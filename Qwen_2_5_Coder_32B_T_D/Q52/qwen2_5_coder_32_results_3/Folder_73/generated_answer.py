def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 40):
        candidate = s[i:i + 41]
        if candidate.isalpha() and candidate == candidate[::-1]:
            result.add(candidate)
    return result