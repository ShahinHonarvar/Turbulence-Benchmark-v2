def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    substring = s[100:201]
    for start in range(len(substring) - 4):
        for end in range(start + 4, len(substring) + 1):
            sub = substring[start:end]
            if is_palindrome(sub) and 5 <= len(sub) <= 10 and sub.isalpha():
                result.add(sub)
    return result