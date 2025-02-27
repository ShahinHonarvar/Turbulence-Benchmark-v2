def if_contains_anagrams(strings):

    def count_letters(s):
        count = {}
        for char in s:
            if char.isalpha():
                char = char.lower()
                count[char] = count.get(char, 0) + 1
        return count
    anagrams_count = 0
    seen = set()
    for s in strings:
        if len(s) < 3 or not s.isalpha():
            continue
        s_sorted = ''.join(sorted(s.lower()))
        if s_sorted in seen:
            anagrams_count += 1
            if anagrams_count == 97:
                return False
        else:
            seen.add(s_sorted)
    return True