def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 337):
        if s[i:i + 338] == s[i:i + 338][::-1]:
            result.add(s[i:i + 338].capitalize())
    return result