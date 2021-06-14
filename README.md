#Blackjack
![](http://clipart-library.com/data_images/415822.jpg)
## Это проект карточная игра BlackJack в Python.
###Требования следующие:
+  Простая текстовая версия игры [Игра Блэк-Джек](https://ru.wikipedia.org/wiki/%D0%91%D0%BB%D1%8D%D0%BA%D0%B4%D0%B6%D0%B5%D0%BA)
+  В игре один игрок против компьютера-дилера (крупье)
+  Игрок может остаться при тех же картах (stand) или запросить ещё карту (hit).
+  Игрок может выбрать сумму, которую он ставит.
+  Нужно следить за общей суммой денег у игрока.
+  Программа информирует игрока о выигрышах, проигрышах, переходе через двадцать один и так далее...
+  Использовала объектно-ориентированное программирование и классы в части кода. Не использовала только функции. Использовала классы для колоды карт и для набора карт у игрока. 

###Последовательность игры
####Чтобы сыграть в Блэкджек, следует выполнить следующие шаги:
1. Создать колоду из 52 карт
2. Перемешать колоду
3. Спросить у Игрока его ставку
4. Убедиться, что ставка Игрока не превышает количество доступных у него фишек
5. Сдать две карты Дилеру и две карты Игроку
6. Показать только одну карту из двух карт Дилера, вторая карта остается скрытой
7. Показать обе карты Игрока
8. Спросить Игрока, хочет ли он взять ещё одну карту (Hit), и если да, то дать ему ещё одну карту
9. Если сумма карт игрока не превышает 21, то спросить его, хочет ли он снова взять ещё одну карту.
10. Если Игрок говорит "хватит" (т.е., дополнительных карт не нужно), то перейти к картам Дилера. Дилер всегда берёт дополнительные карты до тех пор, пока сумма его карт не станет больше или равна 17
11. Определить победителя, и сохранить новое значение для количества фишек у Игрока
12. Спросить Игрока, хочет ли он сыграть снова


####Игральные карты
Стандартная колода карт имеет четыре масти - червы (черви, сердце, Hearts), бубны (буби, бубни, ромби, Diamonds), пики (вини, Spades), трефы (крести, кресты, Clubs), и тринадцать достоинств в каждой масти (от 2 до 10, затем Валет, Дама, Король и Туз). Всего в колоде 52 карты. Валет, Дама и Король имеют каждый 10 очков. Туз имеет либо 11 очков, либо 1 очко таким образом, чтобы получить значение 21 без превышения этого значения. 