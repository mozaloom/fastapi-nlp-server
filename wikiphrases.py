#!/usr/bin/env python

import fire
from nlplogic.corenlp import get_noun_phrases


if __name__ == "__main__":
    fire.Fire(get_noun_phrases)
