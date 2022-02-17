from locators.quote_locators import QuoteLocators as QL

class QuoteParser:	
	def __init__(self, parent):
		self.parent = parent

	def __repr__(self):
		return f'<The quote {self.content} by {self.author}>'

	@property
	def content(self):
		locator = QL.CONTENT_LOCATOR
		return self.parent.select_one(locator).string

	@property
	def author(self):
		locator = QL.AUTHOR_LOCATOR
		return self.parent.select_one(locator).string

	@property
	def tags(self):
		locator = QL.TAGS_LOCATOR
		return self.parent.select_one(locator).string

	# @property
	# def about_author(self):
	# 	locator = QL.ABOUT_LOCATOR
	# 	return self.parent.select_one(locator).attrs['href']
