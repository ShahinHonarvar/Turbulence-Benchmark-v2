from collections import Counter

def palindromes_between_indices(s):
    substring = s[0:4]
    char_counts = Counter(filter(str.isalpha, substring.lower()))
    possible_palindromes = set()
    for char, count in char_counts.items():
        if count >= 2:
            possible_palindromes.add(char * 2 + char)
            if count >= 4:
                possible_palindromes.add(char * 3 + char * 3)
        for char2, count2 in char_counts.items():
            if char != char2 and count2 >= 1:
                possible_palindromes.add(char + char2 + char)
    return {palindrome for palindrome in possible_palindromes if len(palindrome) >= 3}