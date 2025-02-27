def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[103:277]
    result = set()
    for i in range(len(s)):
        for j in range(i + 100, i + 170):
            if j <= len(s):
                subs = s[i:j]
                if subs.isalpha() and subs.lower() == subs[::-1].lower():
                    result.add(subs)
    return result