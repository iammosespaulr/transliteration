import requests
from googletrans import Translator
from unidecode import unidecode

translator = Translator()


def Translit(TextVal = "", LanguageCode = "Tamil", ResultsNo="1"):
    Body = LanguageCodeDict[LanguageCode.upper()]+"-t-i0-und&num="+ResultsNo
    URL = "https://inputtools.google.com/request?text="+TextVal+"&itc="+Body
    r = requests.get(url=URL,)
    data = r.json()
    Input = data[1][0][0]
    Translations = data[1][0][1]
    #print(data[1][0])
    return(Translations[0])

def Translite(text = "" ,LanguageCodedest = 'English',LanguageCodesrc='auto' ):
    data = translator._translate(text, dest=LanguageCodeDict[LanguageCodedest.upper()], src=LanguageCodeDict[LanguageCodesrc.upper()])
    #print(data[0][1])
    return(data[0][1][3])

def CleanText(text):
    """
    Replaces german umlauts and sharp s in given text.
    :param text: text as str
    :return: manipulated text as str
    """
    res = text
    res = res.replace('ä', 'ae')
    res = res.replace('ö', 'oe')
    res = res.replace('ü', 'ue')
    res = res.replace('Ä', 'Ae')
    res = res.replace('Ö', 'Oe')
    res = res.replace('Ü', 'Ue')
    res = res.replace('ß', 'ss')
    return unidecode(res)

def Transliterate( text , LanguageCodedest = "Tamil" , source = "English" ):
    if LanguageCodeDict[LanguageCodedest.upper()] == LanguageCodeDict[source.upper()]:
        return text
    elif LanguageCodeDict[LanguageCodedest.upper()] == 'en':
        #print(CleanText(Translite(text, LanguageCodedest)))
        return CleanText(Translite(text, LanguageCodedest))
    elif LanguageCodeDict[source.upper()] == 'en':
        #print(Translit(text, LanguageCodedest))
        return Translit(text, LanguageCodedest)
    else:
        #print(Translit(CleanText(Translite(text, LanguageCodedest)), LanguageCodedest))
        return Translit(CleanText(Translite(text, LanguageCodedest)), LanguageCodedest)

LanguageCodeDict = {
    'AUTO': 'auto',
    'ENGLISH': 'en',
    'AMHARIC': 'am',
    'ARABIC': 'ar',
    'BENGALI': 'bn',
    'CHINESE': 'zh',
    'GREEK': 'el',
    'GUJARATI': 'gu',
    'HINDI': 'hi',
    'KANNADA': 'kn',
    'MALAYALAM': 'ml',
    'MARATHI': 'mr',
    'NEPALI': 'ne',
    'ORIYA': 'or',
    'PERSIAN': 'fa',
    'PUNJABI': 'pa',
    'RUSSIAN': 'ru',
    'SANSKRIT': 'sa',
    'SINHALESE': 'si',
    'SERBIAN': 'sr',
    'TAMIL': 'ta',
    'TELUGU': 'te',
    'TIGRINYA': 'ti',
    'URDU': 'ur'
}
# if __name__ == '__main__':
#    Transliterate("എൻടെ പേര് മോസസ്", "Tamil", "Malayalam" )
