def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 28):
        sub = s[i:i + 29]
        if sub.isalpha() and sub == sub[::-1]:
            result.add(sub)
    return result