def palindrome_of_length_n(s):

    def is_palindrome(sub_s):
        return sub_s == sub_s[::-1]
    s = s.lower()
    palindrome_substrings = set()
    for i in range(len(s) - 254):
        potential_palindrome = s[i:i + 255]
        if is_palindrome(potential_palindrome):
            palindrome_substrings.add(potential_palindrome)
    return palindrome_substrings