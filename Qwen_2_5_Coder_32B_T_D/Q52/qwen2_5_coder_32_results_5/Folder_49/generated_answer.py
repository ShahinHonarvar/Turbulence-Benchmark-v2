def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 47 + 1):
        sub = s[i:i + 47]
        if sub.isalpha() and sub == sub[::-1]:
            result.add(sub)
    return result