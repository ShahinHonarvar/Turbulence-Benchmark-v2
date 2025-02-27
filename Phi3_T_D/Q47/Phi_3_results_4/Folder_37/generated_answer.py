def palindromes_of_specific_lengths(s):
    s = s.lower()
    sub_s = s[:10]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(sub_s)):
        for len_ in range(3, 6):
            if i + len_ <= len(sub_s) and sub_s[i:i + len_].isalpha():
                if is_palindrome(sub_s[i:i + len_]):
                    palindromes.add(sub_s[i:i + len_])
    return palindromes