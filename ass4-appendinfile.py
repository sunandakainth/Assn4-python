#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Kaint
#
# Created:     19-05-2025
# Copyright:   (c) Kaint 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

data= input("Enter text to write to the file:-")
with open('output.txt' , 'w') as file1:
    writing_file = file1.write(data +'\n')
    print("Data successfully wrritten to output.txt.")
    file1.close()

with open('output.txt', 'r') as file1:
    reading_file = file1.read()
    print(reading_file)
    file1.close()

data1 = input("Enter additional text to append:-")
with open('output.txt' , 'a') as file1:
    writing_file = file1.write(data1 + '\n')
    print("Data successfully appended")
    file1.close()
with open('output.txt', 'r') as file1:
    reading_file = file1.read()
    print(reading_file)
    file1.close()