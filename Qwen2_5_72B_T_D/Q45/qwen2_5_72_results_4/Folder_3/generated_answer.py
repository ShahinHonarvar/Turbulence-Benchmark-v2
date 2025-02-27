def palindromes_between_indices(s):
    substring = s[7:10].lower()
    char_count = {}
    for char in substring:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    possible_palindromes = set()
    for char, count in char_count.items():
        if count >= 2:
            for char2, count2 in char_count.items():
                if count2 >= 2:
                    possible_palindromes.add(char + char2 + char2 + char)
                if count2 == 1 or count2 >= 3:
                    possible_palindromes.add(char + char2 + char)
    return {pal for pal in possible_palindromes if len(pal) >= 3}