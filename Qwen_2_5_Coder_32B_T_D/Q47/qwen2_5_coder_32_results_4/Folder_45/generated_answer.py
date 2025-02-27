def palindromes_of_specific_lengths(s):
    s = s[70:141].lower()
    result = set()
    for i in range(len(s)):
        for l in range(3, 61):
            if i + l <= len(s):
                subs = s[i:i + l]
                if subs.isalpha() and subs == subs[::-1]:
                    result.add(subs)
    return result