# Дашборд с анализом информации о потреблении алкоголя в России (1998-2016)
Проект выполнили студенты группы БСБО-14-21 Фарукшин Эдуард и Гладченко Артем

## Общая информация о датасете
За основу был взят датасет с сайта [kaggle.com](https://www.kaggle.com/). [Ссылка на первоначальный датасет](https://www.kaggle.com/datasets/dwdkills/alcohol-consumption-in-russia/data). Данный датасет содержит информацию о потреблении различных видов алкогольных напитков в разных регионах России за период с 1998 по 2016 год. Данные включают год, регион, а также количество потребленного вина, пива, водки, шампанского и бренди (Потребление = продажи алкоголя в литрах на душу населения). Мы решили добавить в датасет информацию о рождаемости, смертности и урбанизации, для более точного и обширного анализа.
[Скачать датасет](https://docs.google.com/spreadsheets/d/e/2PACX-1vTTYt1uMLU8_Tj0jtrBjdaz1I0U4y_2m4vHGjLJ8OWStP9AuntfQfd00D8zvkcit93OK5ysSIBTlSY2/pub?gid=1669335283&single=true&output=csv)

## Актуальность дашборда
Данный датасет охватывает период с 1998 по 2016 год и предоставляет подробную информацию о потреблении различных видов алкогольных напитков в разных регионах России. Включение данных о рождаемости, смертности и урбанизации делает этот датасет особенно ценным для анализа социально-экономических и демографических тенденций.

### Важность данных
1. **Социально-экономический анализ**: Датасет позволяет исследовать, как изменение потребления алкоголя соотносится с такими показателями, как рождаемость и смертность, что может помочь в разработке социальных и экономических политик.
2. **Региональные различия**: Включение данных по регионам России помогает выявить и понять различия в потреблении алкоголя и их возможные причины.
3. **Урбанизация**: Данные об урбанизации позволяют анализировать влияние урбанизации на потребление алкоголя и демографические показатели.
4. **Временные тренды**: Датасет охватывает 18 лет, что дает возможность изучать долгосрочные тренды и изменения в потреблении алкоголя.

## Актуальные вопросы, решаемые дашбордом

1. **Региональное потребление алкоголя**:
   - Как распределяется потребление различных видов алкоголя по регионам России?
   - Какие регионы потребляют больше всего алкоголя?

2. **Временные тренды в потреблении алкоголя**:
   - Как изменялось потребление вина, пива, водки, шампанского и бренди с 1998 по 2016 год?
   - Какие периоды характеризуются значительными изменениями в потреблении определенных напитков?

3. **Влияние на демографические показатели**:
   - Как потребление алкоголя соотносится с рождаемостью и смертностью по регионам и годам?
   - Есть ли корреляция между уровнем потребления алкоголя и уровнем урбанизации?

4. **Сравнение регионов по ключевым показателям**:
   - Какие регионы лидируют по уровню урбанизации, рождаемости и смертности?
   - Какие регионы имеют наиболее высокие показатели потребления алкоголя?

5. **Общая статистика и процентное соотношение потребления**:
   - Какая доля каждого вида алкоголя в общем объеме потребления?
   - Как изменялось процентное соотношение потребления различных видов алкоголя по годам?


## Общая информация о дашборде
Дашборд состоит из четырех страниц, каждая из которых содержит разнообразные графики и визуализации:

1. **Тепловая карта России**:
   - Динамическая тепловая карта, отображающая потребление алкоголя по регионам России.
   - Слева от карты находятся показатели, выбрав которые, можно увидеть потребление различных видов алкоголя по регионам.
   - Под картой расположен ползунок, позволяющий выбрать конкретный год для более точного анализа.

2. **Линейные диаграммы по видам алкоголя**:
   - Пять отдельных линейных диаграмм, каждая из которых отражает тенденцию потребления определенного вида алкоголя за 18 лет.
   - Эти графики позволяют наглядно увидеть изменения в потреблении каждого напитка по отдельности в зависимости от выбранного региона.

3. **Общая статистика**:
   - Столбчатая диаграмма, показывающая общую статистику по потреблению алкогольных напитков за 18 лет.
   - Круговая диаграмма, отображающая процентное соотношение потребления различных видов алкоголя (с возможностью выбора года).
   - Пузырьковая диаграмма, представляющая соотношение рождаемости и смертности по годам.

4. **Сравнение регионов**:
   - Сравнение всех регионов по таким показателям, как урбанизация, потребление алкоголя, рождаемость и смертность.
   - Топ-10 регионов по указанным показателям для удобства сравнения.
   - Горизонтальная столбчатая диаграмма, отображающая средние показатели потребления алкоголя по всей России за выбранный год.

## Установка и использование
1. **Клонирование репозитория и переход в директорию**:
   ```bash
   git clone https://github.com/PanamCU/RussianAlcoholDashboard.git
   cd RussianAlcoholDashboard

2. **Виртуальное окружение**:
   ```bash
   python3 -m venv venv

3. **Активация виртуального окружения**:
   ```bash
   source venv/bin/activate

4. **Запуск дашборда**:
   ```bash
   python app.py

Помимо этого Вам может потребоваться установить нужные библиотеки, если они у Вас еще не установлены.

## Готовый дашборд, размещенный на хостинге
В качестве интернет платформы для размещения дашборда был использован [PythonAnywhere](https://www.pythonanywhere.com/). Это облачная платформа для разработки и развертывания Python-приложений. Она предоставляет удобный веб-интерфейс для написания, запуска и отладки кода, а также для управления проектами. Итоговый дашборд можно посмотреть по [ссылке](http://russiandashboard.pythonanywhere.com/).
