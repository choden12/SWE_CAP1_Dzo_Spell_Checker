from docx import Document

def convert_docx_to_txt(docx_file, txt_file):
    doc = Document(docx_file)
    
    with open(txt_file, 'w', encoding='utf-8') as f:
        for para in doc.paragraphs:
            f.write(para.text + '\n')

if __name__ == "__main__":
    docx_file = 'dictionary.docx'  
    txt_file = 'dictionary.txt'    
    
    convert_docx_to_txt(docx_file, txt_file)
    print(f"Successfully converted {docx_file} to {txt_file}")
