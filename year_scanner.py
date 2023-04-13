def getYear(string_gendata):
    final_int = "N/A"
    index_last = len(string_gendata) - 1
    for character in string_gendata:
        char_1 = string_gendata[index_last - 3]
        char_2 = string_gendata[index_last - 2]
        char_3 = string_gendata[index_last - 1]
        char_4 = string_gendata[index_last]
        try:
            number_year = int(char_1+char_2+char_3+char_4)
            if number_year > 1000:
                final_int = number_year
                return final_int
        except:
            pass
        index_last = index_last - 1
    return final_int

String_thing = "HMA Aljassas, S Sasi - 2nd International Conference on …, - ieeexplore.ieee.org"
print(getYear(String_thing))
