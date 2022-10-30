def get_count_char(str_):
    str_ = ''.join(str_.lower().split())
    dict_ = {}
    for let in str_:
        if let.isalpha():
            if let in dict_:
                dict_[let] = 1
            else:
                dict_[let] = 1
    return (dict_)


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
