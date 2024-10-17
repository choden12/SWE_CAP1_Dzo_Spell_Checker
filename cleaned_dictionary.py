import re

def clean_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        unique_words = set()
        
        for line in infile:
            cleaned_line = line.strip()

            if not cleaned_line:
                continue
            
            cleaned_line = re.sub(r'[^\u0F00-\u0FFF\s]', '', cleaned_line)

            if cleaned_line not in unique_words:
                unique_words.add(cleaned_line)
                outfile.write(cleaned_line + '\n')

if __name__ == "__main__":
    input_file = 'dictionary.txt'      
    output_file = 'cleaned_dictionary.txt'  
    
    clean_text(input_file, output_file)
    print(f"Successfully cleaned the text. Output saved to {output_file}")
