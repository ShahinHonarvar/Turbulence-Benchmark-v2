def find_palindromes(s):
    res = set()
    s = s.lower()
    for i in range(len(s) - 58):
        substring = s[i:i + 59]
        if substring == substring[::-1]:
            res.add(substring)
    return res

def palindrome_of_length_n(s):
    return find_palindromes(s)