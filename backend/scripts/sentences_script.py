from cgitb import text
import re
import sys
from typing import List
from bs4 import BeautifulSoup
import requests
import csv
import copy
from googletrans import Translator

LEVELS = ["n5","n4", "n3", "n2", "n1"]



def is_excluded(vocab_element: str):
    excluded_list = ['The link', 'Click on', 'This list', "See also", "KATAKANA", "This is", "If you"]
    result_list = re.findall(r"(?=("+'|'.join(excluded_list)+r"))", vocab_element)
    if len(result_list) > 0 or len(vocab_element) < 2:
        return False
    return True


URL = "https://japanesetest4you.com/japanese-language-proficiency-test-jlpt-n2-kanji-exercise-1"
URL2 = "https://japanesetest4you.com/japanese-language-proficiency-test-jlpt-n1-kanji-exercise-2"
URL3 = "https://japanesetest4you.com/japanese-language-proficiency-test-jlpt-n1-kanji-exercise-3"
URL4 = "https://japanesetest4you.com/japanese-language-proficiency-test-jlpt-n5-kanji-exercise-3"
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


# def main():
#     """Echo the input arguments to standard output"""
#     list_of_examples = []
#     for level in LEVELS:
#         level_url = build_url(level)
#         level_text = get_page_vocab(level_url)
#         formated_list = format_to_list(level_text, level)
#         list_of_examples += formated_list

#     with open('backend/test_data/vocabulary_all_levels.csv', 'w', encoding='UTF8', newline='') as f:
#         writer = csv.writer(f, delimiter = ";")
#         # write multiple rows
#         writer.writerows(list_of_examples)
# if __name__ == '__main__':
#     sys.exit(main())  
def get_list_and_answers(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    res1 = soup.find("div", {"class":"entry clearfix"})
    results=soup.find_all('p')
    print(results[3].find_all('input'))
    result_sents = []

    for idx, element in enumerate(results):
            
            if "Answer" in element.text:
                break
            result_sents.append(element.text.split("\n"))

    answers = ""
    for idx, element in enumerate(results):
        if "Question 1:" in element.text: 
            answers= element.text.split("\n")
    return (result_sents, answers)

def clear_lists(dirty_list: List[List[str]]):
    result = copy.deepcopy(dirty_list)
    for main_idx, element in enumerate(dirty_list):
        for idx, sent in enumerate(element):
            if sent=='':
                result[main_idx].pop(idx)
    return result  

def concat_list(whole_list: List[List[str]]):
    result = copy.deepcopy(whole_list)
    for main_idx, element in enumerate(whole_list):
        idx_str= f"{main_idx+1}."
        if not element[0].lstrip()[0].isdigit():
            result[main_idx+1].append(element[0])
    return result

def delete_not_needed(concated_list: List[List[str]]):
    result = []
    for element in concated_list:
        if len(element) > 3:
            result.append(element)
    return result



def make_result_list(clear_list: List[List[str]], answers):
    result = copy.deepcopy(clear_list)
    for idx, element in enumerate(clear_list):
        # print(answers[idx])
        # print("-------")
        ans_idx = int(answers[idx].split(":")[-1].strip())

        # print(ans_idx)
        # # print(element[ans_idx])
        # # print(result[idx])
        # print(element)
        result[idx].append(element[ans_idx].strip())
        result[idx].append('')
        for wa_num in range(4):
            if wa_num+1 == ans_idx:
                continue
            result[idx][-1] = result[idx][-1]+element[wa_num+1].replace("\n","").strip()+","
        result[idx][-1] = result[idx][-1][:-1]
    return result



def keep_sentences_only(sentence_list: List[List[str]]):
    result = []
    for item in sentence_list:
        if len(item) > 7:
            result.append(item)
    return result



def remove_un_elements(sentence_list: List[List[str]]):
    for element in sentence_list:
        del element[1:5]



def clear_kanji(sentence_list: List[List[str]]):
    for element in sentence_list:
        element[0] = element[0].split(".")[1].strip()



def replace_in_sentence(sentence_list: List[List[str]]):
    for element in sentence_list:
        zam = "_"
        zam_f = zam*len(element[0])
        element[1] = element[1].replace(element[0], zam_f)

# print(just_sentences)

def translate(source: str)->str:
    translator = Translator()
    return translator.translate(source, src='ja', dest='en').text

def add_translation(sentence_list: List[List[str]]):
    for element in sentence_list:
        element.append(translate(element[2]))


BASE_URL = "https://japanesetest4you.com/japanese-language-proficiency-test-jlpt-"
def build_url(level: str, number:str)->List[str]:
    return f"{BASE_URL}{level}-kanji-exercise-{number}"

def main():
    to_enter = []
    for level in LEVELS:
        for number in range(19):
            try:
                url = build_url(level, str(number+1))
                results, answers = get_list_and_answers(url)
                cleaned = clear_lists(results)
                concated = concat_list(cleaned)
                clear_list = delete_not_needed(concated)
                # print(len(clear_list))
                # print(len(answers))
                result_list = make_result_list(clear_list, answers)
                just_sentences = keep_sentences_only(result_list)
                remove_un_elements(just_sentences)
                clear_kanji(just_sentences)
                replace_in_sentence(just_sentences)
                add_translation(just_sentences)
                for element in just_sentences:
                    element.append(level)
                # print(just_sentences)
                to_enter += just_sentences
                
            except:
                continue
    to_enter_acc = []
    for element in to_enter:
        if "_" in element[1]:
            to_enter_acc.append(element)
    with open('backend/test_data/sentences_all_levels.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter = ";")
        # write multiple rows
        writer.writerows(to_enter_acc)
if __name__ == '__main__':
    sys.exit(main())  