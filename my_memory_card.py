
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton,QGroupBox,QButtonGroup
from random import shuffle


class Question():
    def __init__(
        self, question, right_answer,
        wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



app = QApplication([])
main_win = QWidget()
main_win.resize(400,300)

text = QLabel('Какой национальности не существует?')
text2 = QPushButton('Ответить')
main_win.cur_question = -1

RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton("Смурфы") 
rbtn_3 = QRadioButton("Чулымцы")
rbtn_4 = QRadioButton("Алеуты") 
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


AnsGroupBox = QGroupBox('Результат теста:')
lb_Result =QLabel('прав или нет')
lb_Correct = QLabel('ответ будет тут')
layout_line4 = QVBoxLayout()
layout_line4.addWidget(lb_Result,alignment=(Qt.AlignLeft))
layout_line4.addWidget(lb_Correct,alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_line4)
AnsGroupBox.hide()


layout_linel = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_linel.addWidget(text, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addStretch(1) 
layout_line3.addWidget(text2, stretch=2) 
layout_line3.addStretch(1)
layout_card = QVBoxLayout() 
layout_card.setSpacing(5)


layout_card = QVBoxLayout() 
layout_card.addLayout(layout_linel) 
layout_card.addLayout(layout_line2, stretch=8) 
layout_card.addStretch(1) 
layout_card.addLayout(layout_line3, stretch=1) 
layout_card.addStretch(1) 
layout_card.setSpacing(5) 


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    text2.setText('Следущий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    text2.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if text2.text() == 'Ответить':
        check_answer()
    else:
        next_question()


answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('ВЕРНО')
        main_win.score +=1
        print('Статистика\n-Всего вопросов: ',main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('НЕВЕРНО')
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')

def show_correct(ans):
    lb_Result.setText(ans)
    show_result()
def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ',main_win.total, '\n-Правильных ответов: ', main_win.score)
    main_win.cur_question += 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)


question_list = []

question_list.append(Question('Как правильно пишется марка мотоцикла',
'DUCATI',
    'DAKACI','BUCATI','DUCATE'))
question_list.append(Question('Максимальная скорость мотоцикла KAWASAKI H2R',
'400км/ч',
    '350км/ч','370км/ч','200км/ч'))
question_list.append(Question('сколько поршней в двигателе питбайка',
'1',
    '4','2','3'))
question_list.append(Question('Какого вида гонок на мотоциклах не существует',
'Гонки на заднем колесе',
    'Шоссейно-кольцевые','Мотокрос','Эндуро'))
question_list.append(Question('Когда был создан 1 мотоцикл',
'1885',
    '1800','2000','1950'))
question_list.append(Question('Существуют ли мотоциклы марки БМВ',
'Да существуют',
    'Нет','БМВ произодит только автомобили','Это бред'))
question_list.append(Question('Самый быстрый мотоцикл в мире ',
'DODGE TOMAHAWL',
    'KAWASAKI H2R','BMW MOTORRAD R 1300 GS','HONDA CB650R'))
question_list.append(Question('Как правильно пишется марка мотоцикла',
'HONDA',
    'HENDA','HONDU','HENDA'))
question_list.append(Question('Какое колесо у мотоцикла является ведущим',
'заднее',
    'переднее','заднее и переднее','его надо толкать'))
question_list.append(Question('Как правильно пишется марка мотоцикла',
'BMW',
    'NBW','WBM','WMB'))


text2.clicked.connect(start_test)
main_win.score = 0
main_win.total = 0
next_question()
main_win.setLayout(layout_card)
main_win.show()
app.exec_()
