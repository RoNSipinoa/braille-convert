import hgtk
import re

'''
이 프로그램은 점자 변환기입니다. 다음과 같은 자료를 참고하여 만들었습니다.

한글점자규정해설서 최종인쇄본(이하 한·점)
'''

letter_CHO = {'ㄱ': '⠈', 'ㄴ': '⠉', 'ㄷ': '⠊', 'ㄹ': '⠐', 'ㅁ': '⠑', 'ㅂ': '⠘', 'ㅅ': '⠠', 'ㅇ': '', 'ㅈ': '⠨',
                   'ㅊ': '⠰', 'ㅋ': '⠋', 'ㅌ': '⠓', 'ㅍ': '⠙', 'ㅎ': '⠚', 'ㄲ': '⠠⠈', 'ㄸ': '⠠⠊', 'ㅃ': '⠠⠘', 'ㅆ': '⠠⠠',
                   'ㅉ': '⠠⠨'}  # 초성 점자 딕셔너리(한·점 제1장 제1항~제3항)
letter_JUNG = {'ㅏ': '⠣', 'ㅑ': '⠜', 'ㅓ': '⠎', 'ㅕ': '⠱', 'ㅗ': '⠥', 'ㅛ': '⠬', 'ㅜ': '⠍', 'ㅠ': '⠩', 'ㅡ': '⠪',
                    'ㅣ': '⠕', 'ㅐ': '⠗', 'ㅔ': '⠝', 'ㅒ': '⠜⠗', 'ㅖ': '⠌', 'ㅘ': '⠧', 'ㅙ': '⠧⠗', 'ㅚ': '⠽', 'ㅝ': '⠏',
                    'ㅞ': '⠏⠗', 'ㅟ': '⠍⠗', 'ㅢ': '⠺', ' ': '⠀'}  # 중성 점자 딕셔너리(한·점 제1장 제7항~제8항)
letter_JONG = {'ㄱ': '⠁', 'ㄳ': '⠁⠄', 'ㄴ': '⠒', 'ㄵ': '⠒⠅', 'ㄶ': '⠒⠴', 'ㄷ': '⠔', 'ㄹ': '⠂', 'ㄺ': '⠂⠁', 'ㄻ': '⠂⠢', 'ㄼ': '⠂⠃',
                    'ㄽ': '⠂⠄', 'ㄾ': '⠂⠦', 'ㄿ': '⠂⠲', 'ㅀ': '⠂⠴', 'ㅁ': '⠢', 'ㅂ': '⠃', 'ㅄ': '⠃⠄', 'ㅅ': '⠄', 'ㅇ': '⠶',
                    'ㅈ': '⠅', 'ㅊ': '⠆', 'ㅋ': '⠖', 'ㅌ': '⠦', 'ㅍ': '⠲', 'ㅎ': '⠴', 'ㄲ': '⠁⠁', 'ㅆ': '⠌', '': ''}  # 종성 점자 딕셔너리 (한·점 제1장 제4항~제6항)
letter_NORMAL = {'.': '⠲', '?': '⠦', '!': '⠖', ',': '⠐', '·': '⠐⠆', ':': '⠐⠂', ';': '⠰⠆', '/': '⠸⠌', '“': '⠦', '”': '⠴',
                 '‘': '⠠⠦', '’': '⠴⠄', '(': '⠦⠄', ')': '⠠⠴', '{': '⠦⠂', '}': '⠐⠴', '[': '⠦⠆', ']': '⠰⠴', '『': '⠰⠦', '《': '⠰⠦', '』': '⠴⠆',
                 '》': '⠴⠆', '「': '⠐⠦', '〈': '⠐⠦', '」': '⠴⠂', '〉': '⠴⠂', '-': '⠤', '―': '⠤⠤', '~': '⠤⠤', '*': '⠔⠔', '※': '⠸⠔', "'": '⠄',
                 '〃': '⠰⠆', '￦': '⠈⠺', '￠': '⠈⠉', '$': '⠈⠙', '￡': '⠈⠇', '￥': '⠈⠽', '€': '⠈⠑'}  # 일반 문자 딕셔너리 (한·점 제44항~제72항)
abbr_CJ = {('ㄱ', 'ㅏ'): '⠫', ('ㄴ', 'ㅏ'): '⠉', ('ㄷ', 'ㅏ'): '⠊', ('ㅁ', 'ㅏ'): '⠑', ('ㅂ', 'ㅏ'): '⠘', ('ㅅ', 'ㅏ'): '⠇', ('ㅈ', 'ㅏ'): '⠨', 
           ('ㅋ', 'ㅏ'): '⠋', ('ㅌ', 'ㅏ'): '⠓', ('ㅍ', 'ㅏ'): '⠙', ('ㅎ', 'ㅏ'): '⠚'}  # 초성 + ㅏ 꼴 약자 딕셔너리 (한·점 제12항)
abbr_JJ = {('ㅓ', 'ㄱ'): '⠹', ('ㅓ', 'ㄴ'): '⠾', ('ㅓ', 'ㄹ'): '⠞', ('ㅕ', 'ㄴ'): '⠡', ('ㅕ', 'ㄹ'): '⠳', ('ㅕ', 'ㅇ'): '⠻',
           ('ㅗ', 'ㄱ'): '⠭', ('ㅗ', 'ㄴ'): '⠷', ('ㅗ', 'ㅇ'): '⠿', ('ㅜ', 'ㄴ'): '⠛', ('ㅜ', 'ㄹ'): '⠯', ('ㅡ', 'ㄴ'): '⠵',
           ('ㅡ', 'ㄹ'): '⠮', ('ㅣ', 'ㄴ'): '⠟', ('ㅓ', 'ㄲ'): '⠹⠁', ('ㅓ', 'ㄳ'): '⠹⠄', ('ㅓ', 'ㄵ'): '⠾⠅', ('ㅓ', 'ㄶ'): '⠾⠴',
           ('ㅓ', 'ㄺ'): '⠞⠁', ('ㅓ', 'ㄻ'): '⠞⠢', ('ㅓ', 'ㄼ'): '⠞⠃', ('ㅓ', 'ㄽ'): '⠞⠄', (' ㅓ', 'ㄾ'): '⠞⠦', ('ㅓ', 'ㄿ'): '⠞⠲',
           ('ㅓ', 'ㅀ'): '⠞⠴', ('ㅕ', 'ㄵ'): '⠡⠅', ('ㅕ', 'ㄶ'): '⠡⠴', ('ㅕ', 'ㄺ'): '⠳⠁', ('ㅕ', 'ㄻ'): '⠳⠢', ('ㅕ', 'ㄼ'): '⠳⠃',
           ('ㅕ', 'ㄽ'): '⠳⠄', ('ㅕ', 'ㄾ'): '⠳⠦', ('ㅕ', 'ㄿ'): '⠳⠲', ('ㅕ', 'ㅀ'): '⠳⠴', ('ㅗ', 'ㄲ'): '⠭⠁', ('ㅗ', 'ㄳ'): '⠭⠄',
           ('ㅗ', 'ㄵ'): '⠷⠅', ('ㅗ', 'ㄶ'): '⠷⠴', ('ㅜ', 'ㄵ'): '⠛⠅', ('ㅜ', 'ㄶ'): '⠛⠴', ('ㅜ', 'ㄺ'): '⠯⠁', ('ㅜ', 'ㄻ'): '⠯⠢',
           ('ㅜ', 'ㄼ'): '⠯⠃', ('ㅜ', 'ㄽ'): '⠯⠄', ('ㅜ', 'ㄾ'): '⠯⠦', ('ㅜ', 'ㄿ'): '⠯⠲', ('ㅜ', 'ㅀ'): '⠯⠴', ('ㅡ', 'ㄵ'): '⠵⠅',
           ('ㅡ', 'ㄶ'): '⠵⠴', ('ㅡ', 'ㄺ'): '⠮⠁', ('ㅡ', 'ㄻ'): '⠮⠢', ('ㅡ', 'ㄼ'): '⠮⠃', ('ㅡ', 'ㄽ'): '⠮⠄', ('ㅡ', 'ㄾ'): '⠮⠦',
           ('ㅡ', 'ㄿ'): '⠮⠲', ('ㅡ', 'ㅀ'): '⠮⠴', ('ㅣ', 'ㄵ'): '⠟⠅', ('ㅣ', 'ㄶ'): '⠟⠴'}  # 중성 + 종성 꼴 약자 리스트 (한·점 제12항)
abbr_CJJ = {('ㄱ', 'ㅓ', 'ㅅ'): '⠸⠎', ('ㄲ', 'ㅓ', 'ㅅ'): '⠠⠸⠎'} # 초성 + 중성 + 종성 꼴 약자 리스트 (한·점 제12항, 제14항)
abbr_WORD = {'그래서': '⠁⠎', '그러나': '⠁⠉', '그러면': '⠁⠒', '그러므로': '⠁⠢',
             '그런데': '⠁⠝', '그리고': '⠁⠥', '그리하여': '⠁⠱'}  # 약어 목록 (한·점 제16항)
each_letter_list = []  # 각각의 글자 객체가 들어가는 리스트


class HangulLetter:  # 한글 객체
    def __init__(self, cho, jung, jong, num):
        self.cho = cho  # 초성
        self.jung = jung  # 중성
        self.jong = jong  # 종성
        self.num = num  # 문장에서의 인덱스
        self.cho_braille = ''  # 초성 점자
        self.jung_braille = ''  # 중성 점자
        self.jong_braille = ''  # 종성 점자
        self.braille = []  # 초+중+종성 점자 합쳐진 리스트

    def compose(self): # 한글 결합
        return hgtk.letter.compose(self.cho, self.jung, self.jong)

    def match(self, cho, jung, jong):  # 주어진 초, 중, 종성과 글자가 일치하는지 체크
        if cho == '' or self.cho == cho:
            if jung == '' or self.jung == jung: 
                if jong == '' or self.jong == jong:
                    return True  # 비어 있는 경우, 항상 일치하는 것으로 간주
        return False

    def rigid_match(self, cho, jung, jong):  # 주어진 초, 중, 종성과 글자가 일치하는지 체크, 단 비어 있는 경우에도 완전히 일치해야 함
        return (self.cho == cho and self.jung == jung and self.jong == jong)

    def has_jong(self):
        return (ord(self.letter) % 28 == 16)

    def jung_headed(self):
        return (self.cho == 'ㅇ' and self.jung != '')


class NormalLetter:  # 한글이 아닌 문자 객체
    def __init__(self, letter, num):
        self.letter = letter  # 글자
        self.num = num  # 문장에서의 인덱스
        self.braille = []  # 글자의 점자 리스트
    
    def match(self, letter):
        return (self.letter == letter)


def abbreviation_cj(letter, cho, jung, repl):  # 초성 + 중성 약자 변환을 위한 함수(한·점 제12항)
    if not letter.match('ㅍ', 'ㅏ', 'ㅆ'): # '팠'의 경우 '폐'와 구별하기 위해 약자로 줄이지 않음 (한·점 제17항)
        if letter.num != len(each_letter_list) - 1:
            if type(each_letter_list[letter.num + 1]) != NormalLetter:
                nextletter = each_letter_list[letter.num + 1]
                if not nextletter.match('ㅇ', 'ㅖ', ''):
                    if not (letter.jung == 'ㅏ' and letter.jong == '') or (letter.match('ㄱ', 'ㅏ', '') or letter.match('ㅅ', 'ㅏ', '') or letter.match('ㅆ', 'ㅏ', '')) or not nextletter.match('ㅇ', '', ''):
                        # 고유 약자 점자가 있는 가, 사, 싸를 제외하고 나머지 초성 + ㅏ는 뒤에 ㅇ + 모음이 오면 ㅏ를 생략하지 않음 (한·점 제17항)
                        if letter.match(cho, jung, ''):
                            # 초성과 중성이 약자와 일치하면 이를 약자로 변환
                            letter.braille = [repl, letter.braille[2]]
            else:
                if letter.match(cho, jung, ''):
                    # 초성과 중성이 약자와 일치하면 이를 약자로 변환
                    letter.braille = [repl, letter.braille[2]]
        else: 
            if letter.match(cho, jung, ''):
                # 초성과 중성이 약자와 일치하면 이를 약자로 변환
                letter.braille = [repl, letter.braille[2]]

def abbreviation_jj(letter, jung, jong, repl):  # 중성 + 종성 약자 변환을 위한 함수(한·점 제12항)
    if any(map(lambda x: letter.match(x, 'ㅕ', 'ㅇ'), ['ㅅ', 'ㅈ', 'ㅊ', 'ㅆ', 'ㅉ'])):
        # 성, 정, 청, 썽, 쩡은 기존 'ㅕ+ㅇ(⠻)'의 약자를 사용하여 표기, 셩, 졍, 쳥, 쎵, 쪙은 약자 사용하지 않음 (한·점 제16항)
        pass
    else:
        if letter.match('', jung, jong):
            letter.braille = [letter.cho_braille, repl]


# 초성 + 중성 + 종성 약자 변환을 위한 함수(한·점 제12항)
def abbreviation_cjj(letter, cho, jung, jong, repl):
    if letter.match(cho, jung, jong):
        letter.braille = [repl]


def braille(message):
    answerstring = ''

    global each_letter_list

    each_letter_list = []

    n = 0

    for i in list(message):  # 문자열을 한글/기타로 나눈 뒤 객체화
        if hgtk.checker.is_hangul(i):
            letter = HangulLetter(*hgtk.letter.decompose(i), n)
            each_letter_list.append(letter)
        else:
            letter = NormalLetter(i, n)
            each_letter_list.append(letter)
        n += 1

    for letter in each_letter_list:  # 점자 변환 실시
        if type(letter) == NormalLetter:
            if letter.match(' '):
                letter.braille.append("⠀")  # 일반 띄어쓰기를 점자용 공점으로
            else:
                for i in letter_NORMAL:
                    if letter.match(i):
                        letter.braille.append(letter_NORMAL[i])  # 기호 변환

        elif type(letter) == HangulLetter:
            if [letter.cho, letter.jung, letter.jong].count('') == 2:  # 자음이나 모음이 단독으로 쓰일 경우 그 앞에 온표 ⠿를 붙여 나타냄 (한·점 제9항)
                if letter.cho == '':
                    letter.braille.append('⠿')
                    letter.jung_braille = letter_JUNG[letter.jung]
                elif letter.jung == '':
                    letter.braille.append('⠿')
                    letter.cho_braille = letter_CHO[letter.cho]
                    if letter.cho == 'ㅇ':
                        letter.cho_braille = '⠛'
            else:
                letter.cho_braille = letter_CHO[letter.cho]
                letter.jung_braille = letter_JUNG[letter.jung]
                letter.jong_braille = letter_JONG[letter.jong]  # 점자로 변환

    for letter in each_letter_list:  # 예외 적용
        prevletter = each_letter_list[letter.num - 1]
        if type(letter) == NormalLetter:
            pass
        else:
            if letter.num != 0 and type(prevletter) == HangulLetter:
                if letter.jung == 'ㅖ' and letter.cho == 'ㅇ' and ord(prevletter.compose()) % 28 == 16:
                    # 모음자에 '예'가 이어 나오면 그 사이에 붙임표 ⠤을 넣음 (한·점 제10항)
                    letter.braille.insert(0, '⠤')

                if letter.jung == 'ㅐ' and letter.cho == 'ㅇ' and prevletter.jong == '':
                    if any(map(lambda x: prevletter.match('ㅇ', x, ''), ['ㅑ', 'ㅘ', 'ㅜ', 'ㅝ'])): # ㅑ, ㅘ, ㅜ, ㅝ에 '애'가 이어 나올 경우 그 사이에 붙임표를 적음 (한·점 제 11항)
                        letter.braille.insert(0, '⠤')

    for letter in each_letter_list:  # 최종 점자 리스트에 합침
        if type(letter) == NormalLetter:
            pass
        else:
            letter.braille.append(letter.cho_braille)
            letter.braille.append(letter.jung_braille)
            letter.braille.append(letter.jong_braille)

    for letter in each_letter_list:  # 약자 적용
        if type(letter) == NormalLetter:
            pass
        else:
            for i in abbr_CJ:  # 초성 + 중성 약자 변환 (한·점 제12항~제14항)
                abbreviation_cj(letter, *i, abbr_CJ[i])
            for i in abbr_JJ:  # 중성 + 종성 약자 변환 (한·점 제12항~제15항)
                abbreviation_jj(letter, *i, abbr_JJ[i])
            for i in ['ㅅ', 'ㅈ', 'ㅊ', 'ㅆ', 'ㅉ']:
                # 성, 정, 청, 썽, 쩡은 기존 'ㅕ+ㅇ(⠻)'의 약자를 사용하여 표기 (한·점 제16항)
                abbreviation_cjj(letter, i, 'ㅓ', 'ㅇ', letter_CHO[i] + '⠻')
            for i in abbr_CJJ:
                # '것'과 '껏'은 고유의 약자 사용 (한·점 제12항, 제14항)
                abbreviation_cjj(letter, *i, abbr_CJJ[i])

    for word in abbr_WORD:
        begin = re.search(f'^({word})', message)
        middle = re.search(f'[^가-힣]({word})', message)
        if begin is not None:  # 약어 적용 - 문두에 나올 시
            index = begin.start()  # 인덱스 값
            for i in word:
                del each_letter_list[index]
            # 빈 한글 객체 생성, 여기에 약어가 들어감
            abbrword = HangulLetter('', '', '', index)
            abbrword.braille = [abbr_WORD[word]]
            each_letter_list.insert(index, abbrword)
            for i in range(len(each_letter_list)):
                each_letter_list[i].num = i  # 인덱스 재설정
        elif middle is not None:  # 약어 적용 - 어중에 나올 시
            index = middle.start() + 1  # 인덱스 값
            for i in word:
                each_letter_list.pop(index)
            abbrword = HangulLetter('', '', '', index)
            abbrword.braille = [abbr_WORD[word]]
            each_letter_list.insert(index, abbrword)

            for i in range(len(each_letter_list)):
                each_letter_list[i].num = i  # 인덱스 재설정
        else:
            pass

    for letter in each_letter_list:
        for k in letter.braille:
            answerstring += k  # 최종 산출이 들어가는 answerstring에 각 문자의 braille에 들어간 리스트에 있는 문자를 하나씩 결합

    return answerstring  # 반환


if __name__ == '__main__':
    while True:
        print(braille(input('점자 변환기:  ')))