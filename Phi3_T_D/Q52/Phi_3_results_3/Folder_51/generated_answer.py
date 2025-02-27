def palindrome_of_length_n(s):
    s = s.lower()
    result_set = set()
    for i in range(len(s) - 72):
        substring = s[i:i + 73]
        if substring == substring[::-1]:
            result_set.add(substring.upper())
    return result_set