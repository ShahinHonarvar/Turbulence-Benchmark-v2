def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    text = text[:5].lower()
    letters = set(text)
    letter_counts = {char: text.count(char) for char in letters}
    palindromes_set = set()
    for char, count in letter_counts.items():
        if count >= 4:
            palindrome_str = char * (count // 2) + (char if count % 2 else '') + char * (count // 2)
            if is_palindrome(palindrome_str):
                palindromes_set.add(palindrome_str)
    return palindromes_set