def palindrome_of_length_at_least_n(s):
    result_set = set()
    s_lower = s.lower()
    for i in range(len(s_lower)):
        for j in range(i + 48, len(s_lower) + 1):
            substr = s_lower[i:j]
            if substr.isalpha() and substr == substr[::-1]:
                result_set.add(substr)
    return result_set