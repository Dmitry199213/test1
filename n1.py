
'''
create_training_sheet("3И", "Математика", "tpl.docx",
                      ("Петров Петр", "5"),
                      ("Иванов Иван", "5"),
                      ("Сергеев Сергей", "3"),
                      ("Никитин Никита", "4"))

'''

from docxtpl import DocxTemplate
import datetime as dt


def create_training_sheet(klass, subject, text, *args):
    doc = DocxTemplate(text)
    context = {
        'class_name': klass,
        'subject_name': subject,
        'marks': [{'num': 1,
    'fio': args[i][0],
    'mark': args[i][1]} for i in range(len(args))]

    }
    doc.render(context)
    doc.save("res.docx")


create_training_sheet("3И", "Математика", "tpl.docx",
                      ("Петров Петр", "5"),
                      ("Иванов Иван", "5"),
                      ("Сергеев Сергей", "3"),
                      ("Никитин Никита", "4"))
