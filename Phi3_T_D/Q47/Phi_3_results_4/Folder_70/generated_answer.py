def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    s = s[10:71].lower()
    for i in range(len(s) - 23):
        for length in range(24, 53):
            if i + length <= len(s):
                sub = s[i:i + length]
                if not sub.isalpha():
                    continue
                if 'a' <= sub[0] <= 'z' and is_palindrome(sub):
                    palindromes.add(sub)
    return palindromes