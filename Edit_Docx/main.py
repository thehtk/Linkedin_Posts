from docx import Document

docx_path = "path.docx"
doc = Document(docx_path)
        
for paragraph in doc.paragraphs:
    if 'ABC' in paragraph.text:
        paragraph.text = paragraph.text.replace('ABC','XYZ')
                
doc.save('output.docx')
