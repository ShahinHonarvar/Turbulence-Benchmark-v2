def if_contains_anagrams(str_list):
    count = 0
    memo = {}

    def is_valid_anagram(s):
        return len(s) >= 3 and ''.join(sorted(s.lower())).isalpha()
    for i in range(len(str_list)):
        now = ''.join(sorted(str_list[i].lower()))
        if now in memo:
            count += memo[now]
            memo[now] += 1
        else:
            memo[now] = 1
    return count <= 464