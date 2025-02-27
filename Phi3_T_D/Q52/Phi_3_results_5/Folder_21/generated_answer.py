def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 406):
        if s[i:i + 407] == s[i:i + 407][::-1]:
            result.add(s[i:i + 407].upper())
    return result