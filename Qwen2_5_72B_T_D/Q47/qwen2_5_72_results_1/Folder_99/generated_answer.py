def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    sub_str = s[127:289]
    palindromes = set()
    for i in range(len(sub_str)):
        for j in range(i + 119, i + 142):
            if j <= len(sub_str):
                sub = sub_str[i:j]
                if sub.isalpha() and is_palindrome(sub.lower()):
                    palindromes.add(sub)
    return palindromes