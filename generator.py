import random


class Password:
    def __init__(self, len_: int,
                 special_characters: bool = False,
                 numbers: bool = False,
                 upper_case_characters: bool = False,
                 count_: int = 1,
                 to_txt: bool = False):

        self.len_ = Password.__validate_len(len_)
        self.special_characters = special_characters
        self.numbers = numbers
        self.upper_case_characters = upper_case_characters
        self.count = Password.__validate_count(count_)
        self.to_txt = to_txt
        self._alphabet = 'abcdefghigklmnopqrstuvyxwz'
        self._alphabet_upper = 'ABCDEFGHIGKLMNOPQRSTUVYXWZ'
        self._num_string = '1234567890'
        self._special_char_strings = '%*()?@#$~!'

    def generate(self):
        str_to_generate = Password._get_str_to_generate(self)

        result = ''

        for __ in range(self.count):
            result += f'{__+1}. '
            for _ in range(self.len_):
                index = random.randint(0, len(str_to_generate)-1)
                result += f'{str_to_generate[index]}'
            result += f'\n'

        if self.to_txt:
            return Password.__insert_to_txt(result)
        return result

    def _get_str_to_generate(self):
        str_to_generate = self._alphabet
        if self.special_characters:
            str_to_generate += self._special_char_strings
        if self.numbers:
            str_to_generate += self._num_string
        if self.upper_case_characters:
            str_to_generate += self._alphabet_upper

        return str_to_generate

    @staticmethod
    def __validate_len(len_):
        if type(len_) is not int:
            try:
                len_ = int(len)
            except:
                raise ValueError('Password len must be integer not %s' % type(len_).__name__)

        if not 1 < len_ < 100:
            raise ValueError(f'Password len must be > 1 and < 100!\n password len = %s' % len_)

        return len_

    @staticmethod
    def __insert_to_txt(text):
        with open(f'result_{random.randint(100, 10000)}.txt', 'w') as file:
            for password in text.split('\n'):
                if password:
                    file.write(f'{password}\n')

        return f'Your passwords are written to a file {file.name}'

    @staticmethod
    def __validate_count(count_):
        if type(count_) is not int:
            try:
                count_ = int(count_)
            except:
                raise ValueError('Password count must be integer not %s' % type(count_).__name__)

        if not 0 < count_ < 100:
            raise ValueError(f'Password count must be > 0 and <100!\n password count = %s' % count_)

        return count_
