from bs4 import BeautifulSoup

from locators.quote_page_locators import QuotePageLocators
from parsers.quotes import QuoteParser

class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        return [QuoteParser(e) for e in self.soup.select(QuotePageLocators.QUOTE)]
