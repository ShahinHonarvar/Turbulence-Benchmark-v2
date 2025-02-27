def palindrome_of_length_n(s):
    s = s.lower()
    result_set = set()
    for i in range(len(s) - 115):
        substring = s[i:i + 116]
        if substring == substring[::-1]:
            result_set.add(substring)
    return result_set