

### Установка на Windows

* Нужен python3.6.

* Установка SpeechRecognition:
```
pip install SpeechRecognition
```

* Установка pocketsphinx: можно скачать [здесь](https://pypi.org/project/pocketsphinx/#files).

* Скачивание обученной модели для русского языка на основе HMM: [здесь](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Russian/). 

Делаем так, чтобы получилась следующая иерархия файлов и каталогов:
```
pocketsphinx-data \
    ru-RU \
        acoustic-model \
            {model' files}
        language-model.lm.bin
        pronounciation-dictionary.dict
```
и подкладываем эти файлы в директорию: `...\AppData\Local\Programs\Python\Python36\Lib\site-packages\speech_recognition\pocketsphinx-data`.

* Запускаем `python main.py`.

---

### Методы работы

* __Google.__ Используя библиотеку `SpeechRecognition`. Нет возможности обработать файлы, которые больше 5 минут. Для некоторых аудио не возвращается ни одного варианта текста. Теоретически в продакшене может понадобиться свой ключ (это платно).

* __Pocketsphinx.__ Используя библиотеку `SpeechRecognition`. Работает локально и очень медленно.

* __Yandex.__ Нужно создавать юридический аккаунт и это платно.

* __Kaldi.__ Нужно попробовать запустить на Ubuntu.
