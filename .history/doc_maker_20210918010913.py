import docx
from docx import Document
from docx.enum.style import WD_BUILTIN_STYLE
from docx.enum.text import WD_COLOR_INDEX
from FastNotes import get_link

doc = Document()

doc.add_heading('Fast Notes')


get_link

entry = Entry(window, width=500, textvariable=link, bd=5)
entry.pack(side = TOP, pady = 5)


doc.save('notes.docx')

