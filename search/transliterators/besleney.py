import re


def besleney_input_normal(field, text):
    """
    Prepare a string from one of the qury fields for subsequent
    processing: replace common shortcuts with valid Adyghe characters.
    """
    # if field not in ('wf', 'lex', 'lex2', 'trans_ru', 'trans_ru2'):
        # return text
    text = re.sub('(?<=[а-яА-ЯёЁӏ])[I1i]', 'ӏ', text)
    text = re.sub('[I1i](?=[а-яА-ЯёЁӏ])', 'ӏ', text)
    # if '*' not in text or re.search('[\\[\\]\\.()]', text) is not None:
        # text = text.replace('уэ', '(о|уэ)')
    return text
