import asyncio, aiohttp
from bs4 import BeautifulSoup
from rich import print


class HangmanSolver:
    """The hangman solver class. You can set interactive to True during __init__ to allow the user to enter the word to guess through an input, else, you must provide the word as a string. For example, if the word is Cake, and you only have the letter e, the input to the function must be '___e'."""

    def __init__(self, interactive: bool = False):
        self.i = interactive

    class Words:
        """The words class, which contains the result of the Solver.
        len:int = the number of possible answers.
        words:list = the list of possible answers.
        query:str = the query used to get the words.
        """

        len: int = 0
        words: list = []
        query: str = ""

    async def solve(self, word: str = None):
        """Finds a list of possible answers from the word given.

        Args:
            word (str, optional): The word to guess.

        Returns:
            Words: The words class containing the results.
        """
        url = "https://wordfind.com/hangman-solver/"
        if self.i:
            print(
                "Enter all known values as letters, and unknown values as _s.\nExample - If the word to guess is 'Cake', and only the letter 'e' is given, you should enter '___e'.\n"
            )
            word = input("")
            wordLen = len(word)
            oldWord = word
            word = word.replace("_", "%3F")

        else:
            wordLen = len(word)
            oldWord = word
            word = word.replace("_", "%3F")
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url,
                data=f"numberOfLetters={wordLen}&word={word}&submit.x=132&submit.y=29",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            ) as resp:
                html = await resp.text()
                soup = BeautifulSoup(html, "html.parser")
                slist = list(soup.find_all("ul", {"class": "cwList"})[0].descendants)
                words = [x.text for x in slist if x.text != ""]
        w = self.Words()
        w.len = len(words)
        w.words = words
        w.query = oldWord
        return w
