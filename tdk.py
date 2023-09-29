import json
import urllib
import urllib.error
import urllib.parse
import urllib.request
from typing import Optional
class TDKError(Exception):
    pass
class WordNotFoundError(TDKError):
    pass
class NetworkError(TDKError):
    pass
CONNECTION_FAILED_MSG = "Bağlanılamadı."
user_agent: Optional[str] = "Mozilla/5.0"
def _get_request(url: str) -> urllib.request.Request:
    return urllib.request.Request(
        url,
        None,
        {"User-Agent": user_agent},
    )
class ara:
    def __init__(self, kelime):
        self.kelime = kelime
        self.atasözü = self.atasözü()
        self.anlam = self.anlam()
        self.anlamlar = self.anlamlar()
        self.örnekler = self.örnekler()
        self.json = self.json()
    def anlam(self):
        word_quoted = urllib.parse.quote(self.kelime)
        data = []
        try:
            req = _get_request("https://sozluk.gov.tr/gts?ara=" + word_quoted)
            with urllib.request.urlopen(req) as res:
                data = []
                j = json.loads(res.read())
                if not isinstance(j, list):
                    raise WordNotFoundError(f"'{self.kelime}' anlamı bulunamadı.")
                data = j
        except urllib.error.URLError as exc:
            raise NetworkError(CONNECTION_FAILED_MSG) from exc
        anlamlar = []
        for i in data[0]["anlamlarListe"]:
            anlam = i['anlam']
            anlamlar.append(anlam)
        return anlamlar[0]
    def anlamlar(self):
        word_quoted = urllib.parse.quote(self.kelime)
        data = []
        try:
            req = _get_request("https://sozluk.gov.tr/gts?ara=" + word_quoted)
            with urllib.request.urlopen(req) as res:
                data = []
                j = json.loads(res.read())
                if not isinstance(j, list):
                    raise WordNotFoundError(f"'{self.kelime}' anlamı bulunamadı.")
                data = j
        except urllib.error.URLError as exc:
            raise NetworkError(CONNECTION_FAILED_MSG) from exc
        anlamlar = []
        for i in data[0]["anlamlarListe"]:
            anlam = i['anlam']
            anlamlar.append(anlam)
        return tuple(anlamlar)
    def örnekler(self):
        word_quoted = urllib.parse.quote(self.kelime)
        data = []
        try:
            req = _get_request("https://sozluk.gov.tr/gts?ara=" + word_quoted)
            with urllib.request.urlopen(req) as res:
                data = []
                j = json.loads(res.read())
                if not isinstance(j, list):
                    raise WordNotFoundError(f"'{self.kelime}' anlamı bulunamadı.")
                data = j
        except urllib.error.URLError as exc:
            raise NetworkError(CONNECTION_FAILED_MSG) from exc
        anlamlar = []
        for i in data[0]["anlamlarListe"]:
            ornlist = []
            if "orneklerListe" in i:
                for x in i["orneklerListe"]:
                    ornlist.append(x['ornek'])
                for y in ornlist:
                    anlamlar.append(y)
        return tuple(anlamlar)
    def atasözü(self):
        word_quoted = urllib.parse.quote(self.kelime)
        data = []
        try:
            req = _get_request("https://sozluk.gov.tr/gts?ara=" + word_quoted)
            with urllib.request.urlopen(req) as res:
                data = []
                j = json.loads(res.read())
                if not isinstance(j, list):
                    raise WordNotFoundError(f"'{self.kelime}' anlamı bulunamadı.")
                data = j
        except urllib.error.URLError as exc:
            raise NetworkError(CONNECTION_FAILED_MSG) from exc
        anlamlar = []
        for i in data[0]["atasozu"]:
            anlamlar.append(i["madde"])
        return tuple(anlamlar)
    def json(self):
        word_quoted = urllib.parse.quote(self.kelime)
        data = []
        try:
            req = _get_request("https://sozluk.gov.tr/gts?ara=" + word_quoted)
            with urllib.request.urlopen(req) as res:
                data = []
                j = json.loads(res.read())
                if not isinstance(j, list):
                    raise WordNotFoundError(f"'{self.kelime}' anlamı bulunamadı.")
                data = j
        except urllib.error.URLError as exc:
            raise NetworkError(CONNECTION_FAILED_MSG) from exc
        return data