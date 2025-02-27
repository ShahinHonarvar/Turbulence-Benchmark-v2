def palindrome_of_length_n(s):
    s = s.lower()
    result_set = set()
    for i in range(len(s) - 46):
        substring = s[i:i + 47]
        if substring.isalpha() and substring == substring[::-1]:
            result_set.add(substring)
    return result_set