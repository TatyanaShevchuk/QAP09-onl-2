class ReadAFile:
    def __init__(self, file_no):
        self.file_no = file_no
        self.arr_no = []

    '''1.Прочитать все файлы'''
    def read(self):
        self.arr_no = []
        with open(self.file_no) as f_no:
            for elem in f_no:
                self.arr_no.append(elem)
        str_no = "".join(self.arr_no).lower()
        return str_no


class MyCounter:
    def __init__(self, file):
        self.file = file
        self.count_letters = 0
        self.count_digits = 0
        self.count_special_symbols = 0
        self.count_punctuation_symbols = 0
        self.count_other_special_symbols = 0
        self.sum_arr_digits = 0
        self.arr_digits = []
        self.arr_special_symbols = []
        self.arr_letters = []
        self.arr_set_letters = []

    '''2. Вывести на экран сколько букв, цифр и спецсимволов в каждом из файлов'''
    def count_file_content(self):
        for content in self.file:
            if content.isalpha():
                self.count_letters += 1
                self.arr_letters.append(content)
            elif content.isdigit():
                self.count_digits += 1
                self.arr_digits.append(int(content))
            else:
                self.count_special_symbols += 1
                self.arr_special_symbols.append(content)
        return f"Letters: {self.count_letters}", \
               f"Digits: {self.count_digits}", \
               f"Special symbols: {self.count_special_symbols}"

    '''Вывести на экран среднее арифметическое всех цифр для каждого из файлов'''
    '''6. Вывести на экран сумму чисел из всех трех файлов'''
    def arith_avr_of_digits(self):
        self.sum_arr_digits = 0
        for digits in self.arr_digits:
            self.sum_arr_digits += int(digits)
        avr_sum = self.sum_arr_digits / len(self.arr_digits)
        return avr_sum

    '''4. Вывести на экран Топ 3 букв для каждого файла (Топ 3 по количеству)'''
    def top_three_letters(self):
        self.arr_set_letters = set(self.arr_letters)
        count_each_letter = []
        for el in self.arr_set_letters:
            count_each_letter.append((self.arr_letters.count(el), el))
        count_each_letter.sort(reverse=True)
        return count_each_letter[:3]

    '''Сравнить количество уникальных букв в каждом файле и вывести на экран в каком файле больше всего
    уникальных.  Если во всех файлах одинаково, вывести на экран, что количество - одинаковое'''
    def unique_letters(self):
        count_unique_letter = 0
        for unique_letter in self.arr_set_letters:
            count_unique_letter += 1
        return count_unique_letter

    '''7. Вывести на экран сколько во всех файлах средт спецсимволов знаков препинания (!-(),.:;?),
    а сколько прочих символов.'''
    def find_special_symbols(self):
        self.count_punctuation_symbols = 0
        self.count_other_special_symbols = 0
        for sign in self.arr_special_symbols:
            if sign in ("!", "-", "(", ")", ",", ".", ":", ";", "?"):
                self.count_punctuation_symbols += 1
            else:
                self.count_other_special_symbols += 1
        return f"Punctuation symbols: {self.count_punctuation_symbols}", \
               f"Other special symbols: {self.count_other_special_symbols}"


f_7 = ReadAFile("file_7.txt")
f_8 = ReadAFile("file_8.txt")
f_9 = ReadAFile("file_9.txt")

counter_7 = MyCounter(f_7.read())
counter_8 = MyCounter(f_8.read())
counter_9 = MyCounter(f_9.read())

print(f"Count file_7 content:", counter_7.count_file_content())
print(f"Count file_8 content:", counter_8.count_file_content())
print(f"Count file_9 content:", counter_9.count_file_content())
print()
print(f"Average sum of digits file_7 is:", counter_7.arith_avr_of_digits())
print(f"Average sum of digits file_8 is:", counter_8.arith_avr_of_digits())
print(f"Average sum of digits file_9 is:", counter_9.arith_avr_of_digits())
print()
print(f"Top three letters in file_7:", counter_7.top_three_letters())
print(f"Top three letters in file_8:", counter_8.top_three_letters())
print(f"Top three letters in file_9:", counter_9.top_three_letters())

unique_num_7 = counter_7.unique_letters()
unique_num_8 = counter_8.unique_letters()
unique_num_9 = counter_9.unique_letters()

print()
print(counter_7.find_special_symbols())
print(counter_8.find_special_symbols())
print(counter_9.find_special_symbols())
print()
print(f"The number of unique letters in file_7 is:", unique_num_7)
print(f"The number of unique letters in file_8 is:", unique_num_8)
print(f"The number of unique letters in file_9 is:", unique_num_9)
if unique_num_7 > unique_num_8 and unique_num_7 > unique_num_9:
    print(f"The file_7 has maximum number of unique letters: {unique_num_7}")
elif unique_num_8 > unique_num_7 and unique_num_8 > unique_num_9:
    print(f"The file_8 has maximum number of unique letters: {unique_num_8}")
elif unique_num_9 > unique_num_7 and unique_num_9 > unique_num_8:
    print(f"The file_9 has maximum number of unique letters: {unique_num_9}")
print()
print(f"The sum of all files digits is:", (counter_7.sum_arr_digits +
                                           counter_8.sum_arr_digits +
                                           counter_9.sum_arr_digits))
print()
print()
print(f"The sum of all punctuation symbols is:", counter_7.count_punctuation_symbols +
      counter_8.count_punctuation_symbols + counter_9.count_punctuation_symbols)
print(f"The sum of all other special symbols is:", counter_7.count_other_special_symbols +
      counter_8.count_other_special_symbols +
      counter_9.count_other_special_symbols)
