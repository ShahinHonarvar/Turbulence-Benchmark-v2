def palindromes_of_specific_lengths(text):

    def is_letter(c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

    def valid_palindrome(palindrome):
        return 20 <= len(palindrome) <= 66 and palindrome == palindrome[::-1] and all((is_letter(c) for c in palindrome))
    return {text[i:j] for i in range(15, 96) for j in range(i + 20, i + 67 + 1) if valid_palindrome(text[i:j].lower())}