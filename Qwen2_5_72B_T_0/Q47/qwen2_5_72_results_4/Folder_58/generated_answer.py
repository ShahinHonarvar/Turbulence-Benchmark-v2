def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[125:284]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 109, i + 127):
            if j <= len(s):
                sub = s[i:j]
                if sub.isalpha() and is_palindrome(sub):
                    palindromes.add(sub)
    return palindromes