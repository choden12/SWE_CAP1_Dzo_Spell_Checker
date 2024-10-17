from docx import Document #Import necessary module for handling .docx files

#convert a .docx file to .txt file
def convert_docx_to_txt(docx_file, txt_file):
    doc = Document(docx_file)
    
    #open the target .txt file 
    with open(txt_file, 'w', encoding='utf-8') as f:
        for para in doc.paragraphs:
            f.write(para.text + '\n')

#check if the scripts is being run directly 
if __name__ == "__main__":
    docx_file = 'dictionary.docx'  
    txt_file = 'dictionary.txt'    
    
    #call the function to perform the conversion
    convert_docx_to_txt(docx_file, txt_file)
    print(f"Successfully converted {docx_file} to {txt_file}")
