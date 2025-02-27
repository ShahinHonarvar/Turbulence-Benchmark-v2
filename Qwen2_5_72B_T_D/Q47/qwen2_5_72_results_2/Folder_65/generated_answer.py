def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[15:96]
    result = set()
    for i in range(len(s)):
        for j in range(i + 20, i + 67):
            if j <= len(s) and s[i:j].isalpha():
                if is_palindrome(s[i:j]):
                    result.add(s[i:j])
    return result