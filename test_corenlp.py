from textblob import TextBlob
from nlplogic.corenlp import (
    get_noun_phrases,
    get_summary,
    search_wikipedia,
    get_textblob,
)


def test_get_noun_phrases():
    # Test with a known Wikipedia page title
    page_title = "Golden State Warriors"
    noun_phrases = get_noun_phrases(page_title)
    assert isinstance(noun_phrases, list)
    assert len(noun_phrases) > 0
    assert all(isinstance(phrase, str) for phrase in noun_phrases)


def test_search_wikipedia():
    # Test with a known query
    query = "Golden State Warriors"
    results = search_wikipedia(query)
    assert isinstance(results, list)
    assert len(results) > 0
    assert all(isinstance(result, str) for result in results)


def test_get_summary():
    # Test with a known Wikipedia page title
    page_title = "Golden State Warriors"
    summary = get_summary(page_title)
    assert isinstance(summary, str)
    assert len(summary) > 0
    assert "Golden State Warriors" in summary


def test_get_textblob():
    # Test with a known text
    text = "The Golden State Warriors are an American professional basketball team based in San Francisco, California."
    blob = get_textblob(text)
    assert isinstance(blob, TextBlob)
    assert len(blob.sentences) > 0
    assert len(blob.noun_phrases) > 0
