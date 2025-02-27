def palindromes_between_indices(s):
    substring = s[2:5].lower()
    char_count = {}
    for char in substring:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    possible_palindromes = set()

    def generate_palindromes(half, odd_char):
        if odd_char:
            palindrome = half + odd_char + half[::-1]
        else:
            palindrome = half + half[::-1]
        if len(palindrome) >= 3:
            possible_palindromes.add(palindrome)

    def backtrack(half, remaining):
        for char, count in remaining.items():
            if count >= 2:
                next_remaining = remaining.copy()
                next_remaining[char] -= 2
                backtrack(half + char, next_remaining)
    backtrack('', char_count.copy())
    if any((char_count[char] % 2 != 0 for char in char_count)):
        for char in char_count:
            if char_count[char] % 2 != 0:
                new_char_count = char_count.copy()
                new_char_count[char] -= 1
                backtrack('', new_char_count)
    return possible_palindromes