def palindromes_between_indices(s):
    substring = s[1:3].lower()
    if len(substring) < 2:
        return set()
    char_count = {}
    for char in substring:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    possible_palindromes = set()

    def generate_palindrome(current, remaining):
        if not any(remaining.values()):
            if len(current) >= 3:
                possible_palindromes.add(current)
            return
        for char, count in remaining.items():
            if count > 0:
                new_remaining = remaining.copy()
                new_remaining[char] -= 2
                generate_palindrome(char + current + char, new_remaining)
    odd_char = [char for char, count in char_count.items() if count % 2 == 1]
    if len(odd_char) > 1:
        return set()
    elif len(odd_char) == 1:
        char_count[odd_char[0]] -= 1
        generate_palindrome(odd_char[0], char_count)
    else:
        generate_palindrome('', char_count)
    return possible_palindromes