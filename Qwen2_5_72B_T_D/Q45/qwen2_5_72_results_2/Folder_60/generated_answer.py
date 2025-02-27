def palindromes_between_indices(s):
    substring = s[3:7]
    char_count = {}
    for char in substring:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    available_chars = ''.join((char * (count // 2) for char, count in char_count.items()))
    results = set()

    def generate_palindrome(prefix, length):
        if length == 0:
            results.add(prefix)
        else:
            for i in range(len(available_chars)):
                new_prefix = prefix + available_chars[i]
                generate_palindrome(new_prefix, length - 2)
    for length in range(4, len(available_chars) * 2 + 1, 2):
        generate_palindrome('', length)
    return set((palindrome + palindrome[-2::-1] for palindrome in results))