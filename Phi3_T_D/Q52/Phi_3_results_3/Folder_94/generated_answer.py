def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    result_set = set()
    for i in range(len(s) - 92):
        if is_palindrome(s[i:i + 93]):
            result_set.add(s[i:i + 93])
    return result_set