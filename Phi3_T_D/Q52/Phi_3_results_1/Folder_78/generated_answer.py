def palindrome_of_length_n(s):
    results = set()
    s_lower = s.lower()
    for i in range(len(s) - 47):
        substr = s_lower[i:i + 48]
        if substr == substr[::-1] and substr.isalpha():
            results.add(substr)
    return results