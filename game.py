from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle
 
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Когда начался третий крестовый поход?', '1189', '1931', '1091', '1661'))
questions_list.append(Question('Кому, по легенде, принадлежит фраза "Если у них нет хлеба, пусть едят пирожные!"?', 'Марии Антуанетте', 'Иосифу Сталину', 'Жану Кальвину', 'Жаку Кальвину'))
questions_list.append(Question('Какой город - столица Австралии?', 'Канберра', 'Сидней', 'Рим', 'Макассар'))
questions_list.append(Question('В кого верят мусульмане?', 'в Аллаха', 'в Иисуса Христа', 'в Будду', 'в Зевса'))
questions_list.append(Question('Сколько длилась столетняя война (учитывая перерывы)?', '116 лет', '100 лет', '117 лет', '284 года'))
questions_list.append(Question('Как будет 5 на двоичном коде?', '101', '5', '11111', '110'))
questions_list.append(Question('Какое движение в Англии?', 'Левостороннее', 'Правостороннее', 'Центральное', 'Поступательное'))
questions_list.append(Question('Как теперь называется Ленинград?', 'Санкт-Петербург', 'Новгород', 'Электросталь', 'Кино'))
questions_list.append(Question('Кто убил Кеннеди?', 'Ли Харви Освальд', 'Пётр I', 'Джордж Буш', 'Мао Дзедун'))
questions_list.append(Question('Как будет по-английски "жить"?', 'live', 'life', 'salt', 'assault'))
questions_list.append(Question('Кто из этих стран граничит с Монголией?', 'Китай', 'Турция', 'Гондурас', 'Тайланд'))
shuffle(questions_list)

app = QApplication([])
 
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!') 
 
RadioGroupBox = QGroupBox("Варианты ответов") 
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1)
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!') 
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) 
 
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) 
    lb_Correct.setText(q.right_answer) 
    show_question() 
 
def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.correct_que += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
 
def next_question():
    print('правилных ответов -', window.correct_que)
    if window.correct_que != 0:
        print('рейтинг -', (window.correct_que / window.cur_question) * 100, '%')
    window.cur_question += 1
    q = questions_list[window.cur_question] 
    ask(q) 

 
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
 
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.cur_question = 0
window.correct_que = 0
 
btn_OK.clicked.connect(click_OK) 
 
next_question()
window.show()
app.exec()