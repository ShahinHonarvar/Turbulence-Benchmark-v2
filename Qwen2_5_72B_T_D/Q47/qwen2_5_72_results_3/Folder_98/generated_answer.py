def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[:21]
    result = set()
    for i in range(len(s)):
        for j in range(i + 5, min(len(s), i + 81)):
            subs = s[i:j]
            if subs.isalpha() and is_palindrome(subs):
                result.add(subs)
    return result