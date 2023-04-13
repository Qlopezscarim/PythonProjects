# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
f = open("Taming of the shrew.txt","r")
lines = []
with open("Taming of the shrew.txt") as f:
    lines = f.readlines()
character_array = ["HORTENSIO","GRUMIO","LUCENTIO","PETRUCHIO","KATHARINA","VINCENTIO","Widow","BIANCA","SLY","Hostess","Lord","First Huntsman","Second Huntsman","Players","A Player","First Servant","Second Servant","Third Servant","Messenger","TRANIO","BAPTISTA","GREMIO","BIONDELLO","Page"]
words_array = [0] * len(character_array)
letters_spoke_array = [0] * len(character_array)
counter = 0
current_index = 0
for line in lines:
    print(counter)
    print(line+"\n")
    counter+=1
    for character in character_array:
        if line.strip() == character.strip():
            current_index = character_array.index(character)
    words_array[current_index] = words_array[current_index] + line.strip().count(" ") + line.count("\n") - 1
    letters_spoke_array[current_index] = letters_spoke_array[current_index] + len(line) - line.count(" ")
    print(words_array)
    print(letters_spoke_array)
arrays_length = len(character_array)
x=0
while x <= arrays_length -1:
    print(str(character_array[x]))
    x = x + 1

# driving book #

f = open("HowDrive.txt")
lines = []
with open("HowDrive.txt") as f:
    lines = f.readlines()
character_array_2 = ["LI\'L BIT.","PECK","LI\'L NT","MALE GREEK CHORUS","FEMALE GREEK CHORUS."]
words_array_2 = [0] * len(character_array_2)
letters_spoke_array_2 = [0] * len(character_array_2)
counter_2 = 0
current_index_2 = 0
for line in lines:
    for character in character_array_2:
        if line.count(character) >>0:
            current_index_2 = character_array_2.index(character)
    words_array_2[current_index_2] = words_array_2[current_index_2] + line.strip().count(" ") + line.count("\n") - 1
    letters_spoke_array_2[current_index_2] = letters_spoke_array_2[current_index_2] + len(line) - line.count(" ")
print(words_array_2)
print(letters_spoke_array_2)

table_1 = np.array([character_array,words_array,letters_spoke_array])
df = pd.DataFrame(table_1)
pd.set_option("display.max_rows", len(character_array), "display.max_columns", len(character_array))
df.to_excel("output_1.xlsx")

table_2 = np.array([character_array_2,words_array_2,letters_spoke_array_2])
df_2 = pd.DataFrame(table_2)
pd.set_option("display.max_rows", len(character_array_2), "display.max_columns", len(character_array_2))
df_2.to_excel("output_2.xlsx")