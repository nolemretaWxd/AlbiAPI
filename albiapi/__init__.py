import requests
from requests_toolbelt import MultipartEncoder
import json

class AlbiclaClient:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.session = requests.session()

    def Login(self):
        loginPage = self.session.get("https://albicla.com/login")
        data = {"email": self.login, "pass": self.password, "signin": "zaloguj"}
        login = self.session.post("https://albicla.com/login", data=data)
        if 'aa_user' in self.session.cookies:
            self.username = login.text.replace("'</script>", '').replace("<script type='text/javascript'>document.location.href='/", '').replace("\n", '')
            self.userID = self.session.cookies['aa_user'].split(".", 1)[0]
        else:
            raise LoginError

    def Post(self, post):
        try:
            self.userID
            self.username
        except AttributeError:
            raise NoUserLoggedIn
        else:
            url = "https://albicla.com/" + self.username
            files = {
                'tid': (None, self.userID),
                'post_text': (None, post),
                'upload': ("", "", 'application/octet-stream'),
                'post_article': (None, ""),
                'post_visible': (None, "3"),
                'post_add': (None, "")
            }
            m = MultipartEncoder(files, boundary="------WebKitFormBoundary7S5Tf9yilHHh1Bod")
            headers = {
                "content-type": m.content_type,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
                "origin": "https://albicla.com",
                "referer": url
            }
            post = self.session.post(url, data=m.to_string(), headers=headers)

    def Search(self, query):
        try:
            self.userID
            self.username
        except AttributeError:
            raise NoUserLoggedIn
        else:
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
                "origin": "https://albicla.com",
                "referer": "https://albicla.com/" + self.username
            }
            queryResponse = self.session.get("https://albicla.com/api/search?q=" + query, headers = headers).text
            return json.loads(queryResponse)

class LoginError(Exception):
    def __init__(self):
        super().__init__("An error occured when logging in")

class NoUserLoggedIn(Exception):
    def __init__(self):
        super().__init__("You need to be logged in.")