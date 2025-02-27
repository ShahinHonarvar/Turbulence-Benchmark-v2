def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 187):
        sub = s[i:i + 188]
        if sub == sub[::-1] and sub.isalpha():
            result.add(sub)
    return result