from PyQt5.QtWidgets import (
    QHBoxLayout, QVBoxLayout,
    QButtonGroup, QRadioButton,
    )


class ButtonGroup(QButtonGroup):
    ''' Релизация чекбокса. '''

    def gen_button(self, answer):
        self.radio_groups = [QRadioButton(text=i) for i in answer]
        return self.radio_groups

    def init_checkbox(self):
        ''' Добавляет созданные кнопки в группу '''
        for i in self.radio_groups:
            self.addButton(i)

    def unpin_button(self):
        """ Сбрасывает группу """
        self.setExclusive(False)  # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
        for i in self.radio_groups:
            i.setChecked(False)
        self.setExclusive(True)  # вернули ограничения.


class QBattonLayout(QVBoxLayout):
    '''
        Панель слоев.
        Реализаци динамической таблицы.
    '''

    def _gen_layout(self, count, coll=2):
        if count % coll == 0:
            max_layout = count // coll
        else:
            max_layout = count // coll + 1
        self.row_layout = [QHBoxLayout() for i in range(max_layout)]

    def fill_layout(self, btn_gr, coll=2):
        self._gen_layout(len(btn_gr), coll)
        for i in range(0, len(self.row_layout)):
            layout = self.row_layout[i]
            for i in range(coll):
                try:
                    layout.addWidget(btn_gr.pop())
                except IndexError:
                    break
            self.addLayout(layout)

class Question():
    '''
        Класс панели вопросса.
        * Адаптер для чекбокса
    '''

    def gen_form(self):
        self.btn_gr = ButtonGroup()
        self.layout = QBattonLayout()
        radio_gr = self.btn_gr.gen_button(self.answer)
        self.layout.fill_layout(radio_gr, self.coll)
        return self.layout

    def get_layout(self):
        if self.lazy:
            self.lazy = False
            return self.gen_form
        else:
            return self.layout

    def clearn_form(self):
        self.btn_gr.unpin_button()

    def __init__(self, question:list, right_answer:str, answer:list, coll=2):
        self.question = question
        self.right_answer = right_answer
        self.answer = answer
        self.lazy = True
        self.coll = coll

    def check_btn(self):
        """ реализация проверки нажатия верной кнопки """
        return True


class QuestionGroup:
    """ Реализации зацылненново генератора. """
    def __init__(self, coll=2):
        self.q = []
        self.count = 0
        self.coll = coll

    def add_question(self, question, right_answer, answer):
        self.q.append(
            Question(question, right_answer, answer, self.coll)
        )

    def get_question(self):
        return self.q[self.count]

    def next_question(self):
        if self.count != len(self.q):
            self.count = 0
        else:
            self.count = 0
        return self.q[self.count]
