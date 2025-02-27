def if_contains_anagrams(word_list):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    count = 0
    lower_bound = 3
    len_wlist = len(word_list)
    for i in range(len_wlist):
        for j in range(i + 1, len_wlist):
            if len(word_list[i]) >= lower_bound and len(word_list[j]) >= lower_bound:
                if is_anagram(word_list[i], word_list[j]):
                    count += 1
    return count >= 140