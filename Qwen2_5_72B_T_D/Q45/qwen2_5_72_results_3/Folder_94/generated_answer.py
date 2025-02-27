def palindromes_between_indices(s):
    substring = s[3:5]
    letter_count = {}
    for char in substring:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_count:
                letter_count[char_lower] += 1
            else:
                letter_count[char_lower] = 1
    possible_palindromes = set()
    for char, count in letter_count.items():
        if count >= 2:
            if count % 2 == 0:
                possible_palindromes.add(char * count)
            else:
                possible_palindromes.add(char * (count - 1))
    return {palindrome for palindrome in possible_palindromes if len(palindrome) >= 3}