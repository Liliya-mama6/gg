from threading import Thread
from time import sleep
from datetime import datetime

def writes_words(word_cout, file_name):
    for i in range(word_cout):
        if i==0:
            file=open(file_name, 'w')
            file.write(f'Какое-то слово № {str(i+1)}')
            sleep(0.1)
        else:
            file=open(file_name, 'a')
            file.write('\n'+f'Какое-то слово № {str(i+1)}')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

a=datetime.now()

writes_words(10, 'example1.txt')
writes_words(30, 'example2.txt')
writes_words(200, 'example3.txt')
writes_words(100, 'example4.txt')

print(f'Работа потоков {datetime.now()-a}')

s_first=Thread(target=writes_words, args=(10, 'example5.txt'))
s_se=Thread(target=writes_words, args=(30, 'example6.txt'))
s_th=Thread(target=writes_words, args=(200, 'example7.txt'))
s_fo=Thread(target=writes_words, args=(100, 'example8.txt'))

a=datetime.now()

s_first.start()
s_se.start()
s_th.start()
s_fo.start()

s_first.join()
s_se.join()
s_th.join()
s_fo.join()

print(f'Работа потоков {datetime.now()-a}')
