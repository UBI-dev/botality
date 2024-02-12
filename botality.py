from dataclasses import dataclass
from urllib.parse import urljoin
from functools import wraps

from requests import Session

URL = "http://127.0.0.1:8000/api"

def CatchAllWrapper(func):
    @wraps(func)
    def wrapper(*a, **kw):
        try:
            return func(*a, **kw)
        except Exception as e:
            raise Exception(f'Caught exception while using wrapper, {e}')    
    return wrapper

@dataclass
class Wrapper:
    """
    API wrapper, that uses tokens and provides
    easier methods for the end user.
    """

    url: str
    token: str
    _session: Session

    def __init__(self, token, url=None):
        """
        Provide the auth Token, to personalize the
        wrapper for the Bot.
        """

        if url is None:
            self.url = URL
        else:
            self.url = urljoin(url, "/api")

        self.token = token
        self._session = Session()
        headers = {'Authorization': f'Token {self.token}'}
        self._session.headers = headers

    @CatchAllWrapper
    def getWallet(self):
        url = self.url + "/wallet/"
        response = self._session.get(url)
        return response.status_code, response.json()

    @CatchAllWrapper
    def getBets(self):
        url = self.url + "/bet/"
        response = self._session.get(url)
        return response.status_code, response.json()

    @CatchAllWrapper
    def createBet(self, amount, bet):
        url = self.url + "/bet/"
        payload = {"amount": amount, "bet": bet}

        response = self._session.post(url, payload)
        return response.status_code, response.json()
    
    @CatchAllWrapper
    def deleteBet(self, bet):
        bet_id = bet['id']
        delete_url = f"{self.url}{bet_id}/"
        response = self._session.delete(delete_url)
        return response.status_code, response.json()

    @CatchAllWrapper
    def getLoans(self):
        url = self.url + "/loan/"
        response = self._session.get(url)
        return response.status_code, response.json()

    @CatchAllWrapper
    def createLoan(self, amount):
        url = self.url + "/loan/"
        payload = {"amount": amount}

        response = self._session.post(url, payload)
        return response.status_code, response.json()

    @CatchAllWrapper
    def deleteLoan(self, loan):
        loan_id = loan['id']
        loan_url = f"{self.url}{loan_id}/"
        response = self._session.delete(loan_url)
        return response.status_code, response.json()
