def palindrome_of_length_n(s):
    s = s.lower()
    result_set = set()
    for i in range(len(s) - 56):
        substring = s[i:i + 57]
        if substring == substring[::-1]:
            result_set.add(substring)
    return result_set