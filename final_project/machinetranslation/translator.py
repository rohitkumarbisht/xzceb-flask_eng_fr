from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''
    This function translates English text to French
    '''
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    '''
    This function translates French text to English
    '''
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
    return english_text