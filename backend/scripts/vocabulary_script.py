import re
import pandas as pd
import sys
from typing import List
from bs4 import BeautifulSoup, element
import requests
import csv

BASE_URL = "https://japanesetest4you.com/jlpt-"
LEVELS = ["n5","n4", "n3", "n2", "n1"]

def build_url(level: str)->List[str]:
    return f"{BASE_URL}{level}-vocabulary-list/"

def is_excluded(vocab_element: str):
    excluded_list = ['The link', 'Click on', 'This list', "See also", "KATAKANA", "This is", "If you"]
    result_list = re.findall(r"(?=("+'|'.join(excluded_list)+r"))", vocab_element)
    if len(result_list) > 0 or len(vocab_element) < 2:
        return False
    return True


URL = "https://japanesetest4you.com/jlpt-n2-vocabulary-list/"

def get_page_vocab(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="entry clearfix")
    return results.getText()



def format_to_list(texts:str, level: str):
    texts_list = texts.split("\n")

    texts_list = [vocab_element.strip() for vocab_element in texts_list if is_excluded(vocab_element)]

    texts_list = [text.replace(";", ",").replace(" (", ";", 1).replace("): ", ";", 1).replace("):\xa0", ";").replace("\xa0(", ";").replace("\u200b", "").split(";", 2) for text in texts_list]
    result_list = []
    for test_text in texts_list:
        if len(test_text) == 3:
            # test_text[2].replace('"', "")
            test_text.append(level)
            result_list.append(test_text)
    return result_list


def main():
    """Echo the input arguments to standard output"""
    list_of_examples = []
    for level in LEVELS:
        level_url = build_url(level)
        level_text = get_page_vocab(level_url)
        formated_list = format_to_list(level_text, level)
        list_of_examples += formated_list

    with open('backend/test_data/vocabulary_all_levels.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter = ";")
        # write multiple rows
        writer.writerows(list_of_examples)
if __name__ == '__main__':
    sys.exit(main())  