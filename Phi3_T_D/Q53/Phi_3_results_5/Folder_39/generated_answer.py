def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i].lower() != s[-(i + 1)].lower():
            return False
    return True

def palindrome_of_length_at_least_n(s: str) -> set:
    s_letters_only = ''.join(filter(str.isalpha, s)).lower()
    return {s_letters_only[i:j] for i in range(len(s_letters_only)) for j in range(i + 69, len(s_letters_only) + 1) if is_palindrome(s_letters_only[i:j])}