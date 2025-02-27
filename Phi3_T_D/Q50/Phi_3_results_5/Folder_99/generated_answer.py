from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_map[sorted_string].append(string)
    for _, string_list in anagram_map.items():
        if len(string_list) > 1:
            for i in range(len(string_list)):
                for j in range(i + 1, len(string_list)):
                    if is_anagram(string_list[i], string_list[j]):
                        anagram_count += 1
                        if anagram_count >= 314:
                            return True
    return False