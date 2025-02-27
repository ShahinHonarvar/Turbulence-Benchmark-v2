def if_contains_anagrams(word_list):

    def count_anagrams(word):
        char_count = [0] * 26
        for char in word.lower():
            if char.isalpha():
                char_count[ord(char) - ord('a')] += 1
        return tuple(char_count)

    def compare_anagrams(anagram_dict):
        anagram_keys = list(anagram_dict.keys())
        anagram_count = 0
        for i in range(len(anagram_keys)):
            for j in range(i + 1, len(anagram_keys)):
                if anagram_dict[anagram_keys[i]] == anagram_dict[anagram_keys[j]]:
                    anagram_count += 1
        return anagram_count
    anagram_dict = {}
    for word in word_list:
        if len(word) >= 3:
            anagram_key = count_anagrams(word)
            anagram_dict.setdefault(anagram_key, []).append(word)
    return compare_anagrams(anagram_dict) >= 96