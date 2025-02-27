def palindrome_of_length_n(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    len_s = len(s)
    palindromes = set()
    for i in range(len_s - 55):
        subs = s[i:i + 56].lower()
        if subs.isalpha() and is_palindrome(subs):
            palindromes.add(subs)
    return palindromes