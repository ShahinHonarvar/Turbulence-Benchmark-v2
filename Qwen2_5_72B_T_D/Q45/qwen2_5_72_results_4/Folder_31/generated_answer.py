from collections import Counter

def palindromes_between_indices(s):
    s_sub = s[1:9]
    counter = Counter(s_sub)
    char_list = list(counter.elements())
    palindromes = set()

    def generate_palindrome(length, path, remaining):
        if len(path) == length:
            if path == path[::-1]:
                palindromes.add(path.lower())
            return
        for char in remaining:
            next_remaining = remaining.copy()
            next_remaining.remove(char)
            generate_palindrome(length, path + char, next_remaining)
    for length in range(6, len(s_sub) + 1):
        generate_palindrome(length, '', char_list.copy())
    return palindromes