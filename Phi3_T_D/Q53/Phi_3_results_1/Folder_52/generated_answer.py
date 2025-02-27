def palindrome_of_length_at_least_n(s):
    result_set = set()
    s = s.lower()
    for i in range(len(s) - 13):
        for j in range(i + 13, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                result_set.add(sub)
    return result_set