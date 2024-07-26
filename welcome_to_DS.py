import pandas as pd
import numpy as np
# а также импортируем модули Seaborn и Matplotlib для работы с графикой.
import matplotlib.pyplot as plt
import seaborn as sns

# Считываем учебный файл и сохраняем его в переменную df.
df = pd.read_csv('https://stepik.org/media/attachments/course/4852/iris.csv')

# Создание графика violinplot.
column = 'petal length'
sns.violinplot(y=df[column], color="purple")

# Отображение графиков Matplotlib и Seaborn в PyCharm.
plt.show()
