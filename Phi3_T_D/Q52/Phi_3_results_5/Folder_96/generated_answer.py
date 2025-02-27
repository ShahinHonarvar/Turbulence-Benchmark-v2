from string import ascii_letters

def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 82):
        if all((c.isalpha() for c in s[i:i + 83])):
            if s[i:i + 83] == s[i:i + 83][::-1]:
                res.add(s[i:i + 83])
    return res