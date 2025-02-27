def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = 96
    for i in range(len(s) - n + 1):
        subs = s[i:i + n]
        if subs == subs[::-1] and subs.isalpha():
            result.add(subs)
    return result