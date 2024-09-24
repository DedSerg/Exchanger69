# import requests
# import pandas
# import numpy as np
# import matplotlib.pyplot as plt
# import numpy as np
from PIL import Image

# requests - запросить данные с сайта и вывести их в консоль.

# imgage = requests.get('https://build-experts.ru/wp-content/uploads/2018/06/normy-rasstojanij-na-uchastke1.jpg')
# with open('dopusk.jpg', 'wb') as f:
#     f.write(imgage.content)

# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.

# df = pandas.read_csv('poems.txt')
# print(df)

# numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.

# a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# print(a)
# print(a + 20)
# print(a>50)
# print(a<50)
# print(a*2)

# matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.

# phi = np.linspace(0, 4.*np.pi, 50)
# plt.plot(phi, np.sin(phi))
# plt.plot(phi, np.cos(phi))
# plt.show()

# pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.

filename = 'dopusk.jpg'
with Image.open(filename) as img:
    img.load()
print(type(img))
print(img.size)
convert_image = img.transpose(Image.FLIP_TOP_BOTTOM)
convert_image.save('dopusk 1.jpg')
rotate_image = img.rotate(45)
rotate_image.save('dopusk 2.jpg')
save_image = img.save('dopusk.png')



