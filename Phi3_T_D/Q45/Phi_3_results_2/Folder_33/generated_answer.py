def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

def get_substrings(s):
    substr_list = []
    for i in range(len(s)):
        for j in range(i + 4, len(s) + 1):
            substr_list.append(s[i:j])
    return substr_list

def create_palindrome_substrings(s):
    palindromes = set()
    for substr in get_substrings(s):
        if len(substr) >= 4 and is_palindrome(substr):
            palindromes.add(substr.lower())
    return palindromes

def palindromes_between_indices(s):
    return create_palindrome_substrings(s[7:10])