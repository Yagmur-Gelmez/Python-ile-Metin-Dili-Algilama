from langdetect import detect

def detect_language(text):
    try:
        lang = detect(text)
        return lang
    except:
        return "Belirsiz"

# Örnek kullanım
text = input("Bir metin giriniz:")

language = detect_language(text)
print("Metin dili:", language)

