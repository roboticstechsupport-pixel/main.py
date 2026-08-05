"""
==========================================================
Project ULTRON
automation/browser.py
==========================================================
"""

import webbrowser
import urllib.parse


class BrowserController:
    """
    Browser automation utilities.
    """

    def __init__(self):

        self.google = "https://www.google.com/search?q={}"
        self.youtube = "https://www.youtube.com/results?search_query={}"
        self.github = "https://github.com/search?q={}"
        self.wikipedia = "https://en.wikipedia.org/wiki/{}"

    ##########################################################

    def open_url(self, url):

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        webbrowser.open(url)

    ##########################################################

    def google_search(self, query):

        url = self.google.format(
            urllib.parse.quote_plus(query)
        )

        webbrowser.open(url)

    ##########################################################

    def youtube_search(self, query):

        url = self.youtube.format(
            urllib.parse.quote_plus(query)
        )

        webbrowser.open(url)

    ##########################################################

    def github_search(self, query):

        url = self.github.format(
            urllib.parse.quote_plus(query)
        )

        webbrowser.open(url)

    ##########################################################

    def wikipedia_search(self, topic):

        topic = topic.replace(" ", "_")

        url = self.wikipedia.format(topic)

        webbrowser.open(url)

    ##########################################################

    def open_gmail(self):

        webbrowser.open("https://mail.google.com")

    ##########################################################

    def open_github(self):

        webbrowser.open("https://github.com")

    ##########################################################

    def open_youtube(self):

        webbrowser.open("https://youtube.com")

    ##########################################################

    def open_google(self):

        webbrowser.open("https://google.com")

    ##########################################################

    def open_chatgpt(self):

        webbrowser.open("https://chatgpt.com")

    ##########################################################

    def open_stackoverflow(self):

        webbrowser.open("https://stackoverflow.com")

    ##########################################################

    def search_maps(self, location):

        url = (
            "https://www.google.com/maps/search/" +
            urllib.parse.quote_plus(location)
        )

        webbrowser.open(url)

    ##########################################################

    def search_news(self, query):

        url = (
            "https://news.google.com/search?q=" +
            urllib.parse.quote_plus(query)
        )

        webbrowser.open(url)

    ##########################################################

    def search_images(self, query):

        url = (
            "https://www.google.com/search?tbm=isch&q=" +
            urllib.parse.quote_plus(query)
        )

        webbrowser.open(url)

    ##########################################################

    def search_scholar(self, query):

        url = (
            "https://scholar.google.com/scholar?q=" +
            urllib.parse.quote_plus(query)
        )

        webbrowser.open(url)
