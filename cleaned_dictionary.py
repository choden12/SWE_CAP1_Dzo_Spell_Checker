import re #Importing the regular expression module

#Clean text by removing unwanted characters and keeping only unique lines
def clean_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        unique_words = set() #Initialize an empty set to store unique lines
        
        #iterate over each line in the input file
        for line in infile:
            cleaned_line = line.strip()

            if not cleaned_line:
                continue #skip the line if it is empty
            
            #Remove any characters that are not in unicode range
            cleaned_line = re.sub(r'[^\u0F00-\u0FFF\s]', '', cleaned_line)

            if cleaned_line not in unique_words:
                unique_words.add(cleaned_line) #if the cleaned is unique add it to the set and write it to the output
                outfile.write(cleaned_line + '\n')

#Main part of the script
if __name__ == "__main__":
    input_file = 'dictionary.txt'      
    output_file = 'cleaned_dictionary.txt'  
    
    #call the clean_text function to process was successful
    clean_text(input_file, output_file)
    print(f"Successfully cleaned the text. Output saved to {output_file}") # cleaning process was successful
