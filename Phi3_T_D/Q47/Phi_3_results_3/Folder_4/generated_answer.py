from string import ascii_letters

def palindromes_of_specific_lengths(s):

    def is_palindrome(subs: str) -> bool:
        return subs == subs[::-1]
    result = set()
    s = s[12:93].lower()
    for length in range(17, 67):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if all((c in ascii_letters for c in substr)) and is_palindrome(substr):
                result.add(substr)
    return result