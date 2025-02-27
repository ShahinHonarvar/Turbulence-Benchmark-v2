def longest_palindrome(s: str) -> str:

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            left -= 1
            right += 1
        return s[left + 1:right]
    longest = ''
    for i in range(len(s)):
        palindrome1 = expand_around_center(i, i)
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome1) >= 78 and len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) >= 78 and len(palindrome2) > len(longest):
            longest = palindrome2
    return longest

def palindrome_of_length_at_least_n(s: str) -> set:
    potential_palindromes = {longest_palindrome(s[i:]) for i in range(len(s))}
    return {palindrome for palindrome in potential_palindromes if len(palindrome) >= 78 and palindrome.isalpha()}