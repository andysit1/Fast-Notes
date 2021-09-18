import docx
from docx import Document
from docx.enum.style import WD_BUILTIN_STYLE
from docx.enum.text import WD_COLOR_INDEX
from FastNotes import get_link



doc = Document()

doc.add_heading('Fast Notes')

get_link



doc.save('notes.docx')

