# simple python script to parse text from exam format and rewrite into new text file
# for easy copy and paste into a single column in spreadsheet, where each cell is
# a question or multiple choice answer

# purpose of this script is to help convert tests in canvas
import re


# input: txt file ONLY
def get_text(file_name):
    file = open(file_name, "r", encoding='utf-8')
    file_text = file.read()
    file.close()
    return file_text


# parse by question and multiple choice answers
# input: string
def parse(txt):
    question = '\d+\.'
    choice_a = '|a\..'
    choice_b = '|b\..'
    choice_c = '|c\..'
    choice_d = '|d\..'
    sep = question + choice_a + choice_b + choice_c + choice_d
    parts = re.split(sep, txt)
    return parts


# write each question/answer in a new line in output file
# input : list of strings
def create_output(parsed_txt):
    file = open(r"C:\Users\<user>\PycharmProjects\<folder>\output.txt", "w", encoding='utf-8')
    for str in parsed_txt:
        if not str.endswith('\n'):
            str = str + '\n'
        file.write(str)
    file.close()


# main
if __name__ == '__main__':
    text = get_text(r'C:\Users\<user>\Downloads\ch3.txt')
    parsed_text = parse(text)
    create_output(parsed_text)



