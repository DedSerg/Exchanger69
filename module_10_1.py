from time import sleep
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = datetime.now()
print(f'Работа функций: {(end_time - start_time).total_seconds()} сек.')
th1 = Thread(target=write_words, args=(10, 'example5.txt'))
th2 = Thread(target=write_words, args=(30, 'example6.txt'))
th3 = Thread(target=write_words, args=(200, 'example7.txt'))
th4 = Thread(target=write_words, args=(100, 'example8.txt'))
start_time = datetime.now()
th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()

end_time = datetime.now()
print(f'Работа функций: {(end_time - start_time).total_seconds()} сек.')
