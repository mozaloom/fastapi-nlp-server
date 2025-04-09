import pytest
from nlplogic.corenlp import get_noun_phrases, get_summary, search_wikipedia, get_textblob

def test_get_noun_phrases():
    # Test with a known Wikipedia page title
    page_title = "Golden State Warriors"
    noun_phrases = get_noun_phrases(page_title)
    assert isinstance(noun_phrases, list)
    assert len(noun_phrases) > 0
    assert all(isinstance(phrase, str) for phrase in noun_phrases)

