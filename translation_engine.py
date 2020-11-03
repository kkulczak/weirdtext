import random
import re
from typing import List

import numpy as np

SEPARATOR = '\n—weird—\n'


def encode(message: str) -> str:
    # Tokenization
    tokenize_re = re.compile(r'(\w+)', re.U)
    tokenized = tokenize_re.finditer(message)

    orig_words = set()
    encoded_message = list(message)

    for match in tokenized:
        word_str = match.group()
        if len(word_str) <= 3:
            continue

        word = list(word_str)
        first, last = word[0], word[-1]

        # Permutation generation
        # We have to make sure to do not use identity perm
        word = np.array(word[1:-1])
        perm = np.random.permutation(len(word))
        while (perm == np.arange(len(word))).all():
            perm = np.random.permutation(len(word))

        # Encoding
        encoded_word = word[perm]
        if "".join(encoded_word) != word_str:
            encoded_message[match.start():match.end()] = [
                first,
                *encoded_word,
                last
            ]
            orig_words.add(word_str)

    return f'{SEPARATOR}{"".join(encoded_message)}{SEPARATOR}' \
           f'{" ".join(list(orig_words))}'


def unique_rep(w: str) -> str:
    return f"{w[0]}{''.join(sorted(w[1:-1]))}{w[-1]}"


def decode(message:str) -> str:
    # Validation
    if len(re.findall(SEPARATOR, message)) != 2:
        raise ValueError('Wrong number of seprarators')
    _, encoded, words = message.split(SEPARATOR)
    if len(_) != 0:
        raise ValueError('Data before first separator')

    # Building translation dictionary
    dictionary = {
        unique_rep(w): w
        for w in (words.split(' ') if len(words) > 0 else [])
    }

    # Tokens Extraction
    tokenize_re = re.compile(r'(\w+)', re.U)
    tokenized = tokenize_re.finditer(encoded)
    decoded = list(encoded)

    # Translation
    for match in tokenized:
        word_str = match.group()
        if len(word_str) <= 3:
            continue

        rep = unique_rep(word_str)
        if rep in dictionary:
            translation = dictionary[unique_rep(word_str)]
            decoded[match.start():match.end()] = list(translation)
    return decoded
