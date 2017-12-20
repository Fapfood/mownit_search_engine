MOwNiT Search Engine
====================

Dataset:
--------

Używam danych z dumpa:
https://archive.org/download/twitter_cikm_2010/twitter_cikm_2010.zip

Z pliku:
training_set_tweets.txt

clean_data.py
-------------

+ czyści dane z dat i userów
+ usuwa wszystkie wpisy zawierające cyfry i odnośniki do innych userów

matrix_builder.py
-----------------

Przebudowuje wpisy na macierz rzadką, w 3 wariantach:
+ przeskalowany przez idf oraz znormalizowany
+ tylko znormalizowany
+ ani przeskalowany, ani znormalizowany (format wymagany przez moduł lda)

ld_allocation.py
----------------

Grupuje słowa w tekstach tematami

svds.py
-------

+ oblicza svd
+ oblicza lra
+ zamienia macierz lra na macierz rzadką

engine.py
---------

Umożlwia wybranie jednego z 4 rodzajów macierzy:
+ przeskalowana i znormalizowana
+ znormalizowana
+ przeskalowana, znormalizowana i przybliżona
+ znormalizowana i przybliżona

Pod adresami / lub /search wprowadzamy zapytanie

Przekierowuje nas do /results i wyświetla wyniki
