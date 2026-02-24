from googletrans import Translator

translator = Translator()

print("=== Text to English Translator ===")

text = input("Enter text: ")
source_lang = input("Enter source language code (ta, hi, kn, te, ml, fr, etc): ")

translated = translator.translate(text, src=source_lang, dest='en')

print("Translated to English:", translated.text)