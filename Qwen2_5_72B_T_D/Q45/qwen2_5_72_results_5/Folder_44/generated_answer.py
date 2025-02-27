from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:8].lower()
    counter = Counter(substring)
    middle_chars = [char for char, count in counter.items() if count % 2 != 0]
    half_palindrome = ''.join([char * (count // 2) for char, count in counter.items()])
    if len(middle_chars) > 1:
        return set()
    palindromes = set()
    if len(middle_chars) == 1:
        for i in range(len(half_palindrome) + 1):
            candidate = half_palindrome[:i] + middle_chars[0] + half_palindrome[i:]
            if len(candidate) >= 3:
                palindromes.add(candidate + candidate[::-1])
    else:
        for i in range(len(half_palindrome) + 1):
            candidate = half_palindrome[:i] + half_palindrome[i:]
            if len(candidate) >= 3:
                palindromes.add(candidate + candidate[::-1])
    return palindromes