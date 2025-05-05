from textblob import TextBlob
import wikipedia


def search_wikipedia(query):
    """
    Search Wikipedia for a given query and return the summary.
    """
    print(f"Searching Wikipedia for: {query}")
    return wikipedia.search(query)


def get_summary(page_title):
    """
    Get the summary of a Wikipedia page.
    """
    print(f"Getting summary for: {page_title}")
    return wikipedia.summary(page_title)


def get_textblob(text):
    """
    Create a TextBlob object for the given text.
    """
    text = "The Golden State Warriors are an American professional basketball team based in San Francisco, California. The Warriors compete in the National Basketball Association (NBA) as a member of the league's Western Conference Pacific Division."
    blob = TextBlob(text)
    return blob


def get_noun_phrases(name):
    """
    Get noun phrases from the TextBlob object.
    """
    text = get_summary(name)
    blob = TextBlob(text)
    return blob.noun_phrases
