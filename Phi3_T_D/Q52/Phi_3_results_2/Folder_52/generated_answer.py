def palindrome_of_length_n(s):
    str_len = len(s)
    lower_s = s.lower()
    result = set()
    p = 0
    q = str_len - 1
    while p < q:
        if lower_s[p:p + 423] == lower_s[p:p + 423][::-1]:
            result.add(lower_s[p:p + 423].capitalize())
        p += 1
        q -= 1
    return result