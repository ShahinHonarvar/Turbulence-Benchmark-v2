from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower().replace(' ', '')) == sorted(str2.lower().replace(' ', ''))
    anagram_count = defaultdict(int)
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(strings[i].replace(' ', '')) >= 3:
                anagram_count[strings[i].lower()] += 1
    return sum((count for count in anagram_count.values())) <= 181