from Q37.qwen2_5_72_results_5.Folder_21.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (759 + 2)
    if 'Q' <= 'm' <= 'h':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(759 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[603:759+1]
    for char in sliced_s:
        if 'Q' <= char <= 'h':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(759*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('Q'), ord('h') + 1))
    for _ in range(759 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('Q'), ord('h') + 1))
    for _ in range(603 + 1):
        s += 'Q'
    for _ in range(759 - 603):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
