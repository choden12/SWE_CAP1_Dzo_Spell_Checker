from docx import Document #Import necessary module for handling .docx files

def convert_docx_to_txt(docx_file, txt_file):
    doc = Document(docx_file) #convert a .docx file into a .txt file extracting the text
    
    #open the .txt file 
    with open(txt_file, 'w', encoding='utf-8') as f:
        for para in doc.paragraphs:
            f.write(para.text + '\n')  # write the paragraph text to the txt file 

#main executation block to run the function
if __name__ == "__main__":
    docx_file = 'DZO.docx'  
    txt_file = 'DZO.txt'    
    
    #call the function to perform the docx to txt conversion
    convert_docx_to_txt(docx_file, txt_file)
    print(f"Successfully converted {docx_file} to {txt_file}")