#!/usr/bin/env python3
import sys
import re

def main():
    """
    Checks if proper number of arguments (1) and type (text file ending in .txt) are provided

    """
    if len(sys.argv) == 2 and sys.argv[1].endswith('.txt'):
        text_file = sys.argv[1]
        return text_file 
    else:
        print("Error: Incorrect number or type of command line argument(s)")
        print("Usage: python script.py <text_file>")
        return

def search(text_file):
  """
    Parses text variable if one text file presented as command line
    argument.

    Searches for words related to heritability within the text

    Parameters
    ----------
    text: file
          The text filed to be searched
    
    Returns
    -------
    str or error
        String of formatted text with line numbers indicating the 
        matched line and matched text within the line
    """
  pattern= r'\b\w*herit\w*\b'
  with open(text_file,'r') as text_in:
      print("Opening text_file and reading to text_in")
      with open('output.txt','w') as out_text: 
          print("Opening output.txt")
          print("Searching")
          for line_num, line in enumerate(text_in, start=1):
              #find words throughout the text
              matches= re.findall(pattern, line, flags= re.IGNORECASE)
              for match in matches:
                    if match != '':
                        out_text.write(f'{line_num}\t{match}\n')
          return out_text            
         
      
if __name__ == '__main__':
    text_file=main()
    if text_file:
        search(text_file)
        print("Done")  