def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]

    def search(s, l, r, result):
        while l >= 0 and r < len(s) and (not result[0]):
            if is_palindrome(s[l:r + 1]):
                result[0] = True
            else:
                l -= 1
                r += 1
        return s[l:r]
    result, center, length = ([False], 0, len(text))
    palindromes = set()
    for i in range(1, length):
        if text[i].isalpha() and text[i - 1].isalpha():
            j = 2 * center - i
            if j >= i:
                s = search(text, j, i, result)
                if len(s) >= 36 and s.isalpha() and all((c.lower() in 'abcdefghijklmnopqrstuvwxyz' for c in s.lower())):
                    palindromes.add(s)
        center = i
    if text[-1].isalpha() and text[-2].isalpha():
        j = 2 * center - length
        s = search(text, j, length - 1, result)
        if len(s) >= 36 and s.isalpha() and all((c.lower() in 'abcdefghijklmnopqrstuvwxyz' for c in s.lower())):
            palindromes.add(s)
    return palindromes