def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[12:57]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 20, i + 22):
            if j <= len(s):
                sub = s[i:j]
                if sub.isalpha() and is_palindrome(sub):
                    palindromes.add(sub)
    return palindromes