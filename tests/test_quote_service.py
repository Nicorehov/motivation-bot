from bot.quote_service import get_random_quote, QUOTES

def test_get_random_quote_returns_one_of_quotes():
    quote = get_random_quote()
    assert quote in QUOTES