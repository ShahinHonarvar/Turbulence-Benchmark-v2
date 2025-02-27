def palindromes_of_specific_lengths(s):
    sub_s = s[43:96]

    def is_palindrome(word):
        return word.lower() == word[::-1].lower() and word.isalpha() and (18 <= len(word) <= 47)
    return {sub_s[i:j] for i in range(len(sub_s)) for j in range(i + 18, min(i + 48, len(sub_s) + 1)) if is_palindrome(sub_s[i:j])}