def palindromes_between_indices(s):
    substring = s[1:3].lower()
    char_count = {}
    for char in substring:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    possible_palindromes = set()
    if len(char_count) == 1:
        char, count = list(char_count.items())[0]
        if count >= 3:
            possible_palindromes.add(char * 3)
    return possible_palindromes