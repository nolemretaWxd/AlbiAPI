import os
try:
    import requests
except ImportError:
    print("Brak biblioteki reequests! Zainstaluj ją za pomocą narzędzia pip")
    os.system("pause")
    exit()

try:
    from requests_toolbelt import MultipartEncoder
except ImportError:
    print("Brak biblioteki reequests_toolbelt! Zainstaluj ją za pomocą narzędzia pip")
    os.system("pause")
    exit()

email = input("Podaj login do serwisu albicla.com: ")
password = input("Podaj hasło: ")
post = input("Podaj treść posta: ")

print("Tworzenie sesji...")
session = requests.Session()

print("Przechodzenie na stronę logowania...")
loginPage = session.get("https://albicla.com/login")

print("Logowanie...")
data = {"email": email, "pass": password, "signin": "zaloguj"}
login = session.post("https://albicla.com/login", data = data)
username = login.text.replace("'</script>", '').replace("<script type='text/javascript'>document.location.href='/", '').replace("\n", '')
print("Zalogowano jako: " + username)

print("Postowanie...")
url = "https://albicla.com/" + username
tid = session.cookies['aa_user'].split(".", 1)[0]
files = {
    'tid': (None, tid),
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
post = session.post(url, data=m.to_string(), headers = headers)
print("Zapostowano!")