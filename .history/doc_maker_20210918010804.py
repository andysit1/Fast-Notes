import docx
from docx import Document
from docx.enum.style import WD_BUILTIN_STYLE
from docx.enum.text import WD_COLOR_INDEX


document = Document()

doc.add_heading('Fast Note')



document.save('notes.docx')

