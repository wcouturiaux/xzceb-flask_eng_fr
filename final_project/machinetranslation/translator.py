'''
A module to translate between English and French using IBM Watson
Language Translator.

'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''This function translates English to French

    Parameters:
    english_text (str): String of Text in English

    Returns:
    str:french_text
    '''
    results = language_translator.translate(
        text= english_text,
        model_id='en-fr'
    ).get_result()
    french_text = results['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''This function translates French to English

    Parameters:
    french_text (str): String of Text in French

    Returns:
    str:english_text
    '''
    results = language_translator.translate(
        text= french_text,
        model_id='fr-en'
    ).get_result()
    english_text = results['translations'][0]['translation']
    return english_text
