# -*- coding: utf-8 -*-

# 10.1 В примере с Netflix сходство между двумя пользователями оценивалось
# по формуле расстояния. Но не все пользователи оценивают
# фильмы одинаково. Допустим, есть два пользователя, Йоги и Пинки,
# вкусы которых совпадают. Но Йоги ставит 5 баллов любому фильму,
# который ему понравился, а Пинки более разборчива и ставит ~пятерки~
# только самым лучшим фильмам. Вроде бы вкусы одинаковые, но
# по метрике расстояния они не являются соседями. Как учесть различия
# в стратегиях выставления оценок?

# ответ - снизить ценность пятерок для Йоги (в книге предлагают повысить
# среднюю для Пинки. Хз хз. Я бы снизил для Йоги - но тут надо смотреть
# наврено в среднем по больнице, если все ставят ближе к 5, то надо
# повышать среднюю Пинки, а если в целом все адекватно ставят - то
# снижать Йоги)

# 10.2 Предположим, Netflix определяет группу ~авторитетов». Скажем ,
# Квентин Тарантино и Уэс Андерсон относятся к числу авторитетов
# Netflix, поэтому их оценки оказывают более сильное влияние, чем
# оценки рядовых пользователей. Как изменить систему рекомендаций,
# чтобы она учитывала повышенную ценность оценок авторитетов?

# ответ - оценивать оценки авторитетов отдельно, а потом брать среднее
# между средней оценкой авторитетов и не средней не авторитетов
# в книге предложили поднять вес оценок, но я хз. Мое имхо,
# у нас есть малое количество авторитетов, допустим
# Квентин и другие поставили оценку 4. А средняя не авторитетов - 5,
# итоговую определить как 4,5. С другой стороны это слишком очевидно будет, так
# что.

# 10.3 У сервиса Netflix миллионы пользователей. Б приведенном ранее
# примере рекомендательная система строилась для пяти ближайших
# соседей. Пять - это слишком мало? Слишком много?

# ответ - чем больше пользователей, тем легче строить рекомендации
# зависит от модели тащемта
# в книжке предложили 
# Ответ: Слишком мало. Если ограничиться малым числом соседей,
# существует высокая вероятность того, что результаты будут искажены.
# Существует хорошее эмпирическое правило: для N пользователей
# следует рассматривать sqrt(N) соседей .