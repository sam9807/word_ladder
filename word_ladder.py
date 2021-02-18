#!/bin/python3

from collections import deque
from copy import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony',
    'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    stack = []   # Create a stack

    if start_word == end_word:
        return [start_word]
    if _adjacent(start_word, end_word):
        return [start_word, end_word]

    s = open(dictionary_file, 'r')
    for word in s.readlines():
        stack.append(word.strip('\n'))
    
    ladder = [startword]
    queue = deque()
    queue.append(ladder)
    while queue:   # While the queue is not empty
        current_queue = queue.popleft()
        for word in set(stack):   # For each word in the dictionary
            if _adjacent(word, current_queue[-1]):   # If word top stack
                if word == end_word:   # If this word is the end word
                    return current_queue + [word]   # Stack and word
                new_queue = copy.deepcopy(current_queue)   # Make a copy
                new_queue.append(word)   # Push the found word onto the copy
                queue.append(new_queue)   # Enqueue the copy
                stack.remove(word)   # Delete word from the dictionary


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if (ladder == []) or (ladder is None):
        return False
    for x, word in enumerate(ladder):
        if x == len(ladder) - 1:
            return True
        else:
            if not _adjacent(word, ladder[x + 1]):
                return False


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    difference = 0
    if len(word1) != len(word2):
        return False
    for x, letter in enumerate(word1):
        if word2[x] != letter:
            difference += 1
    if difference == 1:
        return True
    else:
        return False
