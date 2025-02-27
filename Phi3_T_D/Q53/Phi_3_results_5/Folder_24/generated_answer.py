def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result_set = set()
    n = 53
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and substring == substring[::-1]:
            result_set.add(substring.upper())
    return result_set