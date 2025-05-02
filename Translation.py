from deep_translator import GoogleTranslator

print("Text Translator")
target = input("Enter target language (like 'fr', 'ta', 'en'): ")

print(f"\nTranslating everything to '{target}'. Type 'exit' to quit.\n")

while True:
    text = input("Enter text to translate: ")
    if text.lower() == 'exit':
        print("Goodbye!")
        break

    try:
        translated = GoogleTranslator(source='auto', target=target).translate(text)
        print(f"Translated: {translated}\n")
    except Exception as e:
        print("Translation failed:", e, "\n")
