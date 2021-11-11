from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QPushButton, QLabel)

from layout import QuestionGroup

# Создаем структуру с вопросами
q_gr = QuestionGroup(coll=2)
q_gr.add_question(
    'Национальная хижина якутов', 'Юрта', ['Ураса', 'Юрта', 'Иглу', 'Хата']
)

q_gr.add_question(
    'Какого цвета нет на флаге России', 'Зелёный', ['Ураса', 'Зелёный', 'Иглу', 'Хата']
)

app = QApplication([])

btn_OK = QPushButton('Ответить')  # кнопка ответа

# пример работы с генератором
question = q_gr.get_question()  # получаем вопрос
lb_Question = QLabel(question.question)  # Устанавливаем текст вопроса
RadioGroupBox = QGroupBox("Варианты ответов")  # группа на экране для переключателей с ответами
RadioGroupBox.setLayout(question.get_layout())  # Устанавливаем "слой" с вариантами ответов

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')  # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!')  # здесь будет написан текст правильного ответа

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()  # вопрос
layout_line2 = QHBoxLayout()  # варианты ответов или результат теста
layout_line3 = QHBoxLayout()  # кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()  # скроем панель с ответом, сначала должна быть видна панель вопросов

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)  # кнопка должна быть большой
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  # пробелы между содержимым

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

# все настроено, осталось задать вопрос и показать окно:
window.resize(400, 300)
window.show()
app.exec()
