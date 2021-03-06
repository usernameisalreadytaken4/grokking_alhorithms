# -*- coding: utf-8 -*-

# 8.1 Вы работаете в фирме по производству мебели и поставляете мебель
# по всей стране. Коробки с мебелью размещаются в грузовике. Все
# коробки имеют разный размер, и вы стараетесь наиболее эффективно
# использовать доступное пространство. Как выбрать коробки для того ,
# чтобы загрузка имела максимальную эффективность? Предложите
# жадную стратегию. Будет ли полученное решение оптимальным?

# ответ - засунуть сначала самые большие коробки, а потом средние, потом мелкие
# оптимальным - нет

# 8.2 Вы едете в Европу, и у вас есть семь дней на знакомство с достопримечательностями.
# Вы присваиваете каждой достопримечательности
# стоимость в баллах (насколько вы хотите ее увидеть) и оцениваете
# продолжительность поездки. Как обеспечить максимальную стоимость
# (увидеть все самое важное) во время поездки? Предложите
# жадную стратегию. Будет ли полученное решение оптимальным?

# ответ - здесь скорее подойдет алгоритм дейкстры, потому что у нас есть графы и вес
# правда двойной, но все же. но самый простой - ехать начать с относительно неинтересного
# и закончить самым интересным. тоже нет

# Для каждого из приведенных ниже алгоритмов укажите, является этот
# алгоритм жадным или нет.

# 8.3 Быстрая сортировка.

# ответ - нет

# 8.4 Поиск в ширину.

# ответ - вполне.

# 8.5 Алгоритм Дейкстры.

# ответ - нет (wrong - да)

# 8.6 Почтальон должен доставить письма в 20 домов. Ему нужно найти
# кратчайший путь, проходящий через все 20 домов. Является ли эта
# задача NР-полной?

# ответ - да

# 8.7 Имеется задача поиска максимальной клики в множестве людей ( кликой
# называется множество людей, каждый из которых знаком со всеми
# остальными). Является ли эта задача NР-полной?

# нет, не является. алгоритм широкого поиска поможет - wrong (не поможет, так что да)

# 8.8 Вы рисуете карту США, на которой два соседних штата не могут быть
# окрашены в одинаковый цвет. Требуется найти минимальное количество
# цветов, при котором любые два соседних штата будут окрашены
# в разные цвета. Является ли эта задача NР-полной?

# вообще да