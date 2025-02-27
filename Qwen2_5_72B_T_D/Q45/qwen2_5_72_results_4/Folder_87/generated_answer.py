from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    char_count = Counter(substring)
    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(remaining) == 0:
            if len(current) >= 3:
                palindromes.add(current)
            return
        for char in remaining:
            half_remaining = remaining.replace(char, '', 1)
            generate_palindromes(char + current + char, half_remaining)
    if len(odd_chars) == 1:
        for char, count in char_count.items():
            if char != odd_chars[0]:
                half_remaining = substring.replace(char, '', count // 2).replace(odd_chars[0], '', (char_count[odd_chars[0]] - 1) // 2)
                generate_palindromes(odd_chars[0], half_remaining)
    else:
        for char, count in char_count.items():
            half_remaining = substring.replace(char, '', count // 2)
            generate_palindromes('', half_remaining)
    return palindromes