import pytest
from joke_bot import Bot

@pytest.fixture
def bot():
    return Bot()

def test_tell_joke(bot, text):
    joke = bot.tell_joke()
    assert isinstance(joke, str), "Joke is not a string."
    assert len(joke) > 15, "Joke length is not within the correct range."

def test_rate_joke(bot, text):
    joke = "Whats wrong with nature? It has too many bugs."
    rating = bot.rate_joke(joke)
    assert isinstance(rating, (int, float)), "Rating is not a number."
    assert 0 <= rating <= 10, "Rating is not within the correct range."
