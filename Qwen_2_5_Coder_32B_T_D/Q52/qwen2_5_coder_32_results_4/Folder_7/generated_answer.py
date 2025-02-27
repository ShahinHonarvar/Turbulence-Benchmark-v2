def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 415):
        sub = s[i:i + 416]
        if sub == sub[::-1] and sub.isalpha():
            result.add(sub)
    return result