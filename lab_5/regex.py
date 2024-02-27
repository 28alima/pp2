#1
import re
def match_pattern(input_string):
    pattern = re.compile(r'a*b*')
    match = pattern.fullmatch(input_string)
  
#2  
import re
def match_pattern(input_string):
    pattern = re.compile(r'ab{2,3}')
    match = pattern.fullmatch(input_string)
    
#3
import re
def find_sequences(input_string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    matches = pattern.findall(input_string)
    
#4
import re
def find_sequences(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    matches = pattern.findall(input_string)
    
#5
import re
def match_pattern(input_string):
    pattern = re.compile(r'a.*b$')
    match = pattern.fullmatch(input_string)

#6
import re
def replace_chars(input_string):
    pattern = re.compile(r'[ ,.]')
    replaced_string = pattern.sub(':', input_string)
   
#7
import re
def snake_to_camel(snake_case):
    camel_case = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_case)
    return camel_case

#8
import re
def split_at_uppercase(input_string):
    split_result = re.findall(r'[A-Z][a-z]*', input_string)
    return split_result

#9
import re
def insert_spaces(input_string):
    modified_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return modified_string

#10
import re
def camel_to_snake(camel_case):
    snake_case = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case).lower()
    return snake_case
