def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result_set = set()
    len_s = len(s)
    for i in range(len_s):
        for j in range(i + 59, len_s + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result_set.add(substring)
    return result_set