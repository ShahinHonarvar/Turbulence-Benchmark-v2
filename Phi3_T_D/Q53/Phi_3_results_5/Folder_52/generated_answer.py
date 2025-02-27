def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    result_set = set()
    for i in range(length):
        for j in range(i + 13, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result_set.add(substring)
    return result_set