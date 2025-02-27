def palindromes_of_specific_lengths(s):
    s = ''.join(filter(str.isalpha, s[:7])).lower()
    p = set()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 7, len(s)) + 1):
            ss = s[i:j]
            if ss == ss[::-1]:
                p.add(ss)
    return p