def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs.lower() == subs[::-1].lower()
    result = set()
    s_sub = s[100:301]
    for i in range(len(s_sub) - 99):
        subs = s_sub[i:i + 100]
        if is_palindrome(subs):
            result.add(subs)
    return result