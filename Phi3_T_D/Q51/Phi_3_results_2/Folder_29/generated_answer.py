def if_contains_anagrams(strings):

    def ascii_to_int(s):
        return tuple(sorted((ord(char) for char in s.lower())))
    counted_anagrams = {}
    for string in strings:
        if len(string) >= 3:
            ascii_tuple = ascii_to_int(string)
            if ascii_tuple in counted_anagrams:
                counted_anagrams[ascii_tuple] += 1
            else:
                counted_anagrams[ascii_tuple] = 1
    return sum((count * (count - 1) // 2 for count in counted_anagrams.values())) <= 318