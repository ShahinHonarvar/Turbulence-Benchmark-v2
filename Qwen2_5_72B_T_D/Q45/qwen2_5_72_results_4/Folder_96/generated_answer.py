from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    char_count = Counter(substring)
    possible_palindromes = set()

    def can_form_palindrome(chars):
        odd_counts = sum((1 for count in chars.values() if count % 2 != 0))
        return odd_counts <= 1

    def generate_palindromes(chars, path='', used_Characters={}):
        if sum(used_Characters.values()) == sum((count // 2 for count in chars.values())):
            palindrome = path + ''.join([char * (chars[char] % 2) for char in chars]) + path[::-1]
            possible_palindromes.add(palindrome)
            return
        for char in chars:
            if used_Characters[char] < chars[char] // 2:
                used_Characters[char] += 1
                generate_palindromes(chars, path + char, used_Characters)
                used_Characters[char] -= 1
    if can_form_palindrome(char_count):
        generate_palindromes(char_count, '', Counter())
    return possible_palindromes