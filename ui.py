import Note

def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return Note.Note(title=title, body=body)

def menu():
    print("""Это программа 'Заметки'. Имеются следующие функции:
                1 - вывод всех заметок из файла
                2 - добавление заметки
                3 - удаление заметки
                4 - редактирование заметки
                5 - выборка заметок по дате
                6 - показать заметку по id
                7 - выход
             Введите номер функции: """)

def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text

def goodbuy():
    print("Выключение...")