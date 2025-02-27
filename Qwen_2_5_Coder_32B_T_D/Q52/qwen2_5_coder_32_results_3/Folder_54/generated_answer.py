def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n - 84):
        sub = s[i:i + 85]
        if sub == sub[::-1] and sub.isalpha():
            result.add(sub)
    return result