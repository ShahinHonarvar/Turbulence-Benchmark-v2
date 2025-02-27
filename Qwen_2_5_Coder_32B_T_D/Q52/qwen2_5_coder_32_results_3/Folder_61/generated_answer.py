def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 74 + 1):
        subs = s[i:i + 74]
        if subs.isalpha() and subs == subs[::-1]:
            result.add(subs)
    return result