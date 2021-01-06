import hgtk.const

'''
이 프로그램은 점자 변환기입니다. 다음과 같은 자료를 참고하여 만들었습니다.

한글점자규정해설서 최종인쇄본(이하 한·점)
'''

braille_kor_CHOJUNG = {'ㄱ': '⠈', 'ㄴ': '⠉', 'ㄷ': '⠊', 'ㄹ': '⠐', 'ㅁ': '⠑', 'ㅂ': '⠘', 'ㅅ': '⠠', 'ㅇ': '', 'ㅈ': '⠨',
                       'ㅊ': '⠰', 'ㅋ': '⠋', 'ㅌ': '⠓', 'ㅍ': '⠙', 'ㅎ': '⠚', 'ㄲ': '⠠⠈', 'ㄸ': '⠠⠊', 'ㅃ': '⠠⠘', 'ㅆ': '⠠⠠',
                       'ㅉ': '⠠⠨',
                       'ㅏ': '⠣', 'ㅑ': '⠜', 'ㅓ': '⠎', 'ㅕ': '⠱', 'ㅗ': '⠥', 'ㅛ': '⠬', 'ㅜ': '⠍', 'ㅠ': '⠩', 'ㅡ': '⠪',
                       'ㅣ': '⠕', 'ㅐ': '⠗', 'ㅔ': '⠝', 'ㅒ': '⠜⠗', 'ㅖ': '⠌', 'ㅘ': '⠧', 'ㅙ': '⠧⠗', 'ㅚ': '⠽', 'ㅝ': '⠏',
                       'ㅞ': '⠏⠗', 'ㅟ': '⠍⠗', 'ㅢ': '⠺', ' ': '⠀'}  # 초성·중성 점자 리스트(한·점 제 1장 제1항~제3항, 제7항~제8항)
braille_kor_JONG = {'ㄱ': '⠁', 'ㄳ': '⠁⠄', 'ㄴ': '⠒', 'ㄵ': '⠒⠅', 'ㄶ': '⠒⠴', 'ㄷ': '⠔', 'ㄹ': '⠂', 'ㄺ': '⠂⠁', 'ㄻ': '⠂⠢', 'ㄼ': '⠂⠃',
                    'ㄽ': '⠂⠄', 'ㄾ': '⠂⠦', 'ㄿ': '⠂⠲', 'ㅀ': '⠂⠴', 'ㅁ': '⠢', 'ㅂ': '⠃', 'ㅄ': '⠃⠄', 'ㅅ': '⠄', 'ㅇ': '⠶',
                    'ㅈ': '⠅', 'ㅊ': '⠆', 'ㅋ': '⠖', 'ㅌ': '⠦', 'ㅍ': '⠲', 'ㅎ': '⠴', 'ㄲ': '⠁⠁', 'ㅆ': '⠌', '': ''}  # 종성 점자 리스트 (한·점 제1장 제4항~제6항)
abbr_list_cho_cj = ['ㄱ', 'ㄴ', 'ㄷ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅈ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']  # 초성 + ㅏ 꼴 약자 리스트 - 초성
abbr_list_braille_cj = ['⠫', '⠉', '⠊', '⠑', '⠘', '⠇', '⠨', '⠋', '⠓', '⠙', '⠚']  # 초성 + ㅏ 꼴 약자 리스트 - 점자
abbr_list_jung_jj = ['ㅓ', 'ㅓ', 'ㅓ', 'ㅕ', 'ㅕ', 'ㅕ', 'ㅗ', 'ㅗ', 'ㅗ', 'ㅜ', 'ㅜ', 'ㅡ', 'ㅡ', 'ㅣ']  # 중성 + 종성 꼴 약자 리스트 - 중성
abbr_list_jong_jj = ['ㄱ', 'ㄴ', 'ㄹ', 'ㄴ', 'ㄹ', 'ㅇ', 'ㄱ', 'ㄴ', 'ㅇ', 'ㄴ', 'ㄹ', 'ㄴ', 'ㄹ', 'ㄴ']  # 중성 + 종성 꼴 약자 리스트 - 종성
abbr_list_braille_jj = ['⠹', '⠾', '⠞', '⠡', '⠳', '⠻', '⠭', '⠷', '⠿', '⠛', '⠯', '⠵', '⠮', '⠟']  # 중성 + 종성 꼴 약자 리스트 - 점자
abbr_list_jung_add_jj = ['ㅓ', 'ㅓ', 'ㅓ', 'ㅓ', 'ㅓ', 'ㅓ', 'ㅓ', 'ㅓ', 'ㅓ', 'ㅓ', 'ㅓ', 'ㅕ', 'ㅕ', 'ㅕ', 'ㅕ', 'ㅕ', 'ㅕ',
                         'ㅕ', 'ㅕ', 'ㅕ', 'ㅗ', 'ㅗ', 'ㅗ', 'ㅗ', 'ㅜ', 'ㅜ', 'ㅜ', 'ㅜ', 'ㅜ', 'ㅜ', 'ㅜ', 'ㅜ', 'ㅜ', 'ㅡ',
                         'ㅡ', 'ㅡ', 'ㅡ', 'ㅡ', 'ㅡ', 'ㅡ', 'ㅡ', 'ㅡ', 'ㅣ', 'ㅣ']  # 중성 + 종성 꼴 약자(종성 병서) 리스트 - 중성 (한·점 제15항)
abbr_list_jong_add_jj = ['ㄲ', 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ',
                         'ㄾ', 'ㄿ', 'ㅀ', 'ㄲ', 'ㄳ', 'ㄵ', 'ㄶ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㄵ',
                         'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㄵ', 'ㄶ']  # 중성 + 종성 꼴 약자(종성 병서) 리스트 - 종성  (한·점 제15항)
abbr_list_braille_add_jj = ['⠹⠁', '⠹⠄', '⠾⠅', '⠾⠴', '⠞⠁', '⠞⠢', '⠞⠃', '⠞⠄', '⠞⠦', '⠞⠲', '⠞⠴', '⠡⠅', '⠡⠴', '⠳⠁', '⠳⠢', '⠳⠃', '⠳⠄',
                            '⠳⠦', '⠳⠲', '⠳⠴', '⠭⠁', '⠭⠄', '⠷⠅', '⠷⠴', '⠛⠅', '⠛⠴', '⠯⠁', '⠯⠢', '⠯⠃', '⠯⠄', '⠯⠦', '⠯⠲', '⠯⠴', '⠵⠅',
                            '⠵⠴', '⠮⠁', '⠮⠢', '⠮⠃', '⠮⠄', '⠮⠦', '⠮⠲', '⠮⠴', '⠟⠅', '⠟⠴']  # 중성 + 종성 꼴 약자(종성 병서) 리스트 - 점자  (한·점 제15항)
abbr_list_cho_cjj = ['ㄱ', 'ㄲ']  # 초성 + 중성 + 종성 꼴 약자 리스트 - 초성
abbr_list_jung_cjj = ['ㅓ', 'ㅓ']  # 초성 + 중성 + 종성 꼴 약자 리스트 - 중성
abbr_list_jong_cjj = ['ㅅ', 'ㅅ']  # 초성 + 중성 + 종성 꼴 약자 리스트 - 종성
abbr_list_braille_cjj = ['⠸⠎', '⠠⠸⠎']  # 초성 + 중성 + 종성 꼴 약자 리스트 - 점자
normal_list_letter = ['.', '?', '!', ',', ':', ';']
normal_list_braille = ['⠲', '⠦', '⠖', '⠐', '⠐⠂', '⠰⠆']
each_letter_list = []  # 각각의 글자 객체가 들어가는 리스트


class HangulLetter:  # 한글 객체
    def __init__(self, cho, jung, jong, num):
        self.cho = cho  # 초성
        self.jung = jung  # 중성
        self.jong = jong  # 종성
        self.num = num  # 문장에서의 인덱스
        self.list = [cho, jung, jong]  # 초성, 중성, 종성 리스트
        self.cho_braille = ''  # 초성 점자
        self.jung_braille = ''  # 중성 점자
        self.jong_braille = ''  # 종성 점자
        self.braille = []  # 초+중+종성 점자 합쳐진 리스트


class NormalLetter:  # 한글이 아닌 문자 객체
    def __init__(self, thisnamewillnotbeused):
        self.letter = thisnamewillnotbeused  # 글자
        self.braille = []  # 글자의 점자 리스트
        self.cho = ''
        self.jung = ''
        self.jong = ''  # 호환용


letter = HangulLetter('', '', '', -1)  # abbreviation 함수와의 호환을 위한 잉여 letter 객체


async def abbreviation(cho, jung, jong, repl, mode='jj'):  # 점자 약자 변환을 위한 함수(한·점
    global letter
    if mode == 'cj':  # 초성 + 중성 약자
        print(letter.num, letter.cho, letter.jung, letter.jong)
        if letter.cho not in ['ㄱ', 'ㅅ', 'ㅆ'] and letter.jung == 'ㅏ' and letter.jong == '' and letter.num != len(each_letter_list) - 1:
            if each_letter_list[letter.num + 1].cho == 'ㅇ':
                pass  # 고유 약자 점자가 있는 가, 사, 싸를 제외하고 나머지 초성 + ㅏ는 뒤에 ㅇ+모음이 오면 ㅏ를 생략하지 않음 (한·점 제17항)
            elif letter.cho == cho and letter.jung == jung:
                letter.braille = [repl, letter.braille[2]]  # 초성과 중성이 약자와 일치하면 이를 약자로 변환

        elif letter.cho == 'ㅍ' and letter.jung == 'ㅏ' and letter.jong == 'ㅆ':
            pass  # '팠'의 경우 '폐'와 구별하기 위해 약자로 줄이지 않음 (한·점 제17항)

        else:
            if letter.cho == cho and letter.jung == jung:
                letter.braille = [repl, letter.braille[2]]  # 초성과 중성이 약자와 일치하면 이를 약자로 변환
    elif mode == 'cjj':  # 초성 + 중성 + 종성 약자
        if letter.cho == cho and letter.jung == jung and letter.jong == jong:
            letter.braille = [repl]

    elif mode == 'jj':  # 중성 + 종성 약자
        if letter.cho in ['ㅅ', 'ㅈ', 'ㅊ', 'ㅆ', 'ㅉ'] and letter.jung == 'ㅕ' and letter.jong == 'ㅇ':
            pass  # 성, 정, 청, 썽, 쩡은 기존 ᅟᅧᆼ의 약자를 사용하여 표기, 셩, 졍, 쳥, 쎵, 쪙은 약자 사용하지 않음 (한·점 제16항)
        else:
            if letter.jung == jung and letter.jong == jong:
                letter.braille = [letter.cho_braille, repl]


async def braille(message):
    answerstring = ''

    global letter
    global each_letter_list

    each_word_list = []
    each_letter_list = []

    n = -1
    
    for i in list(message):  # 문자열을 한글/기타로 나눈 뒤 음절 단위로 나눔
        if hgtk.checker.is_hangul(i):
            each_word_list.append(list(hgtk.letter.decompose(i)) + ['hangul'])
        else:
            each_word_list.append(list(i) + ['mis'])

    for letterlist in each_word_list:  # 각 음절 객체화
        n += 1  # 인덱스 업데이트
        if letterlist[-1] == 'hangul':
            letter = HangulLetter(letterlist[0], letterlist[1], letterlist[2], n)
            each_letter_list.append(letter)
        elif letterlist[-1] == 'mis':
            letter = NormalLetter(letterlist[0])
            each_letter_list.append(letter)

    for letter in each_letter_list:  # 점자 변환 실시
        if type(letter) == NormalLetter:
            if letter.letter == ' ':
                letter.braille.append("⠀")  # 일반 띄어쓰기를 점자용 공점으로
            else:
                for i in range(len(normal_list_letter)):
                    if letter.letter == normal_list_letter[i]:
                        letter.braille.append(normal_list_braille[i])  # 기호 변환
        elif type(letter) == HangulLetter:
            if letter.list.count('') == 2:
                if letter.cho == '':
                    letter.braille.append('⠿')
                    letter.jung_braille = braille_kor_CHOJUNG[letter.jung]
                elif letter.jung == '':
                    letter.braille.append('⠿')
                    letter.cho_braille = braille_kor_CHOJUNG[letter.cho]  # 자음이나 모음이 단독으로 쓰일 경우 그 앞에 온표 ⠿를 붙여 나타냄 (한·점 제9항)
                    if letter.cho == 'ㅇ':
                        letter.cho_braille = '⠛'
            else:
                letter.cho_braille = braille_kor_CHOJUNG[letter.cho]
                letter.jung_braille = braille_kor_CHOJUNG[letter.jung]
                letter.jong_braille = braille_kor_JONG[letter.jong]  # 점자로 변환

    for letter in each_letter_list:  # 예외 적용
        if type(letter) == NormalLetter:
            pass
        else:
            if letter.num != 0:
                if letter.jung == 'ㅖ' and letter.cho == 'ㅇ' and each_letter_list[letter.num - 1].jong == '' and each_letter_list[letter.num - 1].jung != '':
                    letter.braille.append('⠤')  # 모음자에 '예'가 이어 나오면 그 사이에 붙임표 ⠤을 넣음 (한·점 제10항)

                if letter.jung == 'ㅐ' and letter.cho == 'ㅇ' and each_letter_list[letter.num - 1].jong == '':
                    if each_letter_list[letter.num - 1].jung == '⠜' or each_letter_list[letter.num - 1].jung == '⠧' or \
                            each_letter_list[letter.num - 1].jung == '⠍' or each_letter_list[letter.num - 1].jung == '⠏':
                        letter.braille.append('⠤')  # ㅑ, ㅘ, ㅜ, ㅝ에 '애'가 이어 나올 경우 그 사이에 붙임표를 적음 (한·점 제 11항)

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
            for i in range(len(abbr_list_cho_cj)):  # 초성 + 중성 약자 변환 (한·점 제12항~제14항)
                await abbreviation(abbr_list_cho_cj[i], 'ㅏ', '', abbr_list_braille_cj[i], 'cj')
            for i in range(len(abbr_list_jung_jj)):  # 중성 + 종성 약자 변환 (한·점 제12항~제15항)
                await abbreviation('', abbr_list_jung_jj[i], abbr_list_jong_jj[i], abbr_list_braille_jj[i], 'jj')
            for i in range(len(abbr_list_jung_add_jj)):  # 중성 + 종성 약자 변환 (한·점 제12항~제15항)
                await abbreviation('', abbr_list_jung_add_jj[i], abbr_list_jong_add_jj[i], abbr_list_braille_add_jj[i], 'jj')
            for i in ['ㅅ', 'ㅈ', 'ㅊ', 'ㅆ', 'ㅉ']:
                await abbreviation(i, 'ㅓ', 'ㅇ', '⠻')  # 성, 정, 청, 썽, 쩡은 기존 ᅟᅧᆼ의 약자를 사용하여 표기 (한·점 제16항)
            for i in range(len(abbr_list_jung_cjj)):
                await abbreviation(abbr_list_cho_cjj[i], abbr_list_jung_cjj[i], abbr_list_jong_cjj[i], abbr_list_braille_cjj[i], 'cjj')  # '것'과 '껏'은 고유의 약자 사용 (한·점 제12항, 제14항)

    for letter in each_letter_list:
        for k in letter.braille:
            answerstring += k  # 최종 산출이 들어가는 answerstring에 각 문자의 braille에 들어간 리스트에 있는 문자를 하나씩 결합

    print(answerstring)  # 출력

if __name__ == '__main__':
    braille(input('점자 변환기:  '))
