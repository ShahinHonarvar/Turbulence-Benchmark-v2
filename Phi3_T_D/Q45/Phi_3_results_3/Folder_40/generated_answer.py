def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    substring = s[4:10]
    letter_counts = {}
    for char in substring:
        if char.isalpha():
            char_lower = char.lower()
            letter_counts[char_lower] = letter_counts.get(char_lower, 0) + 1
    middle_char = ''
    half_length = len(substring) // 2
    for char, count in letter_counts.items():
        if count % 2 != 0 and middle_char is None:
            middle_char = char
            letter_counts[char] -= 1
    possible_permutations = ['']
    for char, count in letter_counts.items():
        perms = []
        for _ in range(count):
            for perm in possible_permutations:
                perms.append(perm + char)
            possible_permutations = perms[:]
    palindromes = set()
    for perm in possible_permutations:
        if len(perm) + 1 == half_length + int(middle_char):
            palindrome_half = perm + middle_char + perm[::-1]
            if is_palindrome(palindrome_half):
                palindromes.add(palindrome_half)
    final_palindromes = {p[:7] for p in palindromes if len(p) >= 7}
    return final_palindromes