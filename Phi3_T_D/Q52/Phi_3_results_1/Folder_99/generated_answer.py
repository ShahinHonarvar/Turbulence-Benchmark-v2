def palindrome_of_length_n(s):

    def is_palindrome(subs):
        return subs.lower() == subs[::-1].lower()
    palindromes = {s[i:i + 420] for i in range(len(s) - 419) if is_palindrome(s[i:i + 420]) and s[i:i + 420].isalpha()}
    return palindromes