def palindrome_of_length_n(s):

    def is_palindrome(l, r):
        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    length = len(s)
    palindromes = set()
    for i in range(length - 84):
        if is_palindrome(i, i + 84):
            palindromes.add(s[i:i + 85])
    return palindromes