from collections import defaultdict

def if_contains_anagrams(string_list):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def valid_length(s):
        return len(s) >= 3
    anagram_counts = defaultdict(int)
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if valid_length(string_list[i]) and valid_length(string_list[j]) and are_anagrams(string_list[i], string_list[j]):
                anagrams_key = ''.join(sorted(string_list[i].lower()))
                anagram_counts[anagrams_key] += 1
    return sum((1 for count in anagram_counts.values() if count >= 2)) <= 41