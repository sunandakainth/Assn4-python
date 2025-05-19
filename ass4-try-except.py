#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kaint
#
# Created:     19-05-2025
# Copyright:   (c) Kaint 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

try:
    with open("sample.txt", "r") as file:
        reading_content = file.read()
        print(reading_content)
        file.close()
except FileNotFoundError:
    print("The sample.txt file was not found.")

