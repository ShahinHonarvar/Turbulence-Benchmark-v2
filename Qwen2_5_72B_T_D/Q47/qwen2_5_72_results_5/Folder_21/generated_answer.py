def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[100:296]
    result = set()
    for i in range(len(s)):
        for j in range(i + 136, i + 161):
            if j <= len(s):
                candidate = s[i:j].lower()
                if candidate.isalpha() and is_palindrome(candidate):
                    result.add(candidate)
    return result