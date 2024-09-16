"""Please work on this code again """

filename = r'C:\Users\HP\Desktop\Word of elders.docx'

with open(filename, 'rb', errors='ignore') as file_object:
    files = file_object.readlines()
    for file in files:
         print(file)

  
    
  