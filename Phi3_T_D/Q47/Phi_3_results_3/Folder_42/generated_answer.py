from string import ascii_letters

def palindromes_of_specific_lengths(s):

    def is_palindrome(substr: str) -> bool:
        i, j = (0, len(substr) - 1)
        while i < j:
            if substr[i].lower() not in ascii_letters or substr[j].lower() not in ascii_letters:
                return False
            if substr[i].lower() != substr[j].lower():
                return False
            i += 1
            j -= 1
        return True
    return {s[i:j + 1].lower() for i in range(43, min(96, len(s) - 11)) for j in range(i + 17, min(96, len(s) - 1)) if is_palindrome(s[i:j + 1])}