

### Варианты

* Google Speech API - в документации нет упоминания. Для работы нужен только developer key. Он получается через консоль разработчика. Там же нужно активировать работу с этим API, но такой возможности уже нет ([информация здесь](http://www.chromium.org/developers/how-tos/api-keys)). В репозитории `SpeechRecognition` указан чей-то ключ, пока работает, но теоретически в любой момент его могут отключить (добавлен 5 лет назад). С аудио больше 5 минут не работает, приходится разбивать на куски. Не со всеми аудио работает, помогает разбивание на небольшие куски.
* Yandex SpeechKit - [калькулятор](https://cloud.yandex.ru/services/speechkit#calculator). Посекундная оплата, 15 секунд - 15 рос. рублей. Нужно регистрировать аккаунт на юридическое лицо.
* Google Cloud Speech API - [pricing](https://cloud.google.com/speech-to-text/pricing). 60 минут в месяц - бесплатно, дальше - 0.006 доллара за 15 секунд. Тоже нужен аккаунт для юридического лица, но можно заполнить произвольными данными. Для аудио больше 1 минуты требуется использовать S3 бакет для хранения.
* Pocketsphinx - работает локально, медленно и очень плохо.

Программы:
* [Google Docs](https://www.google.by/intl/ru/docs/about/).
* [RealSpeaker.net](https://realspeaker.net/) - 8 рос. рублей - минута. 1.5 минуты - бесплатно.
* [Zapisano.org](https://app.zapisano.org/guest/transcript) - 29 рос. рублей - 1 рабочий день.
* [Voco](https://www.speechpro.ru/product/programmy-dlya-raspoznavaniya-rechi-v-tekst/voco) - 15500 рос. рублей на год. Многопользовательская версия - 56000 рос. рублей.

Обучение моделей:
* deepspeech от mozilla
* wav2letter от facebook
* kaldi от какого-то университета

Проблемы:
* нет данных для обучения
* нужно машины с GPU и большим количесвом RAM для видеокарт
* нужны люди, которые могут разобраться, как запустить обучение

### Установка на Windows

* Нужен python3.6.

* Установка `SpeechRecognition`:
```
pip install SpeechRecognition
```

[Документация](https://pypi.org/project/SpeechRecognition/).

* Установка `pocketsphinx`: можно скачать [здесь](https://pypi.org/project/pocketsphinx/#files).

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

* Установка `logmmse`.
```
pip install logmmse
```
[Документация](https://pypi.org/project/logmmse/).

* Установка клиента для `Google Cloud`.
```
pip install google
```

##### Настройка ключа для авторизации в Google Cloud Speech API

* Заходим в [консоль разработчика](https://console.cloud.google.com/).
* В поиске ищем "Speech-to-Text API", выбираем и активируем.
* В появившемся окне выбираем пункт меню "Credentials" и создаём "Service Account". ~~При создании выбираем роль "Storage Admin" (эта роль позволяет получить доступ по uri к файлам в бакете).~~
* Добавляем JSON-ключ в аккаунт, скачиваем и подкладываем файл в директорию credentials под названием key.json.
* ~~В консоле разработчика в поиске ищем "Storage".~~
* ~~Создаем бакет и добавляем туда файлы с аудио в формате flac.~~

* Варианты запуска:
```
python main.py --file={path\to\wav-file} denoise
python main.py --file={path\to\wav-file} recognize --type={google,sphinx,google.cloud} [--duration={duration}]
```

---

### Методы работы

* __Google.__ Используя библиотеку `SpeechRecognition`. Нет возможности обработать файлы, которые больше 5 минут. Для некоторых аудио не возвращается ни одного варианта текста.

* __Pocketsphinx.__ Используя библиотеки `SpeechRecognition` и `Pocketsphinx`. Работает локально и очень медленно.

* __Google Cloud.__ Используя библиотеку `Google`.

---

### Примеры работы

|        | kaggle/early_short_stories_0001.wav |
|--------|-------------------------------------|
|Оригинал| За столицей мудрого царя Соломона шелестел по склонам холмов густой лес. С его опушки запутанные тропинки вели на поляну. |
|Google | за столицей Мудрого царя Соломона шелестел по склонам холмов густой лес с его опушке запутанные тропинке в Ильино поляна                                     |
|Sphinx | со столицей мудрого царя соломона шелестел по склонам холмов густой лес с его опушки запутанные тропинки вели на поляну |

|        | kaggle/early_short_stories_0002.wav |
|--------|-------------------------------------|
|Оригинал| Где происходили свидания Ариэля и Тамары. Ему было около 14 лет и ей тоже. |
|Google  | где происходили свидания Ариэль а это Мары ему было около 14 лет и ей то |
|Sphinx | где происходили свидания и карьере и тамара ему было около четырнадцати лет визитёр |

|        | kaggle/early_short_stories_0003.wav |
|--------|-------------------------------------|
|Оригинал| Но Ариэль был сыном знатного иерусалимца, одного из любимейших советников премудрого царя. |
|Google  | Ну Ариэль был сыном знатного Иерусалимская одного из любимейших советников премудрова Царя |
|Sphinx  | но арелет был сыном знатного ерусалим сам одного из любезнейший советников премудрого царя |

|        | kaggle/early_short_stories_0004.wav |
|--------|-------------------------------------|
|Оригинал| Его волосы были черны как ночь, а глаза - как уголь. А Тамара жила за городом, потому что её отцу-иноплеменнику. |
|Google  | его волосы были черны Как ночь А глаза как уголь а Тамара жила за городом потому что её отцу иноплеменников |
|Sphinx  | его волосы были черны как ночь глаза как у уголь а тамара жила за городом потому что её отцу иноплеменников |

|        | kaggle/early_short_stories_0005.wav |
|--------|-------------------------------------|
|Оригинал| Недозволялось обитать среди иудеев. Её мягкие длинные локоны были нежного тёмно-каштанового цвета. |
|Google  | не дозволялось обитать среди иудеев её мягкие длинные локоны были нежного темно каштанового цвета |
|Sphinx  | не дозволялось обитать среди иудеев её менять чьи длинные локоны были нежного темно каштанового цвета |

|        | decoder-test.wav |
|--------|------------------|
|Оригинал| Илья Ильф Евгений Петров Золотой телёнок. |
|Google  | Илья Ильф Евгений Петров Золотой телёнок  |
|Sphinx  | илья ильф евгений петров и золотой телёнок|

|        | videoregistrator.wav |
|--------|----------------------|
|Оригинал|                      |
|Google duration=30 | почитал было Единый классификатор для поиска это было уговаривать уже при наличии слева трамвайных путей попутного направления расположенных на одном уровне с проезжей части поворот налево и разворот и должны выполняться из этих путей если знаками 5.8 не предписанный порядок движения при этом не должно создаваться препятствие трамваев поворот должен осуществляться таким образом чтобы пересечения проезжих частей транспортное средство не оказалось на стороне встречного движения при повороте направо транспортное средство должно двигаться ближе к правому краю проезжей части перед поворотом налево или разворота вне перекрестка водитель безрельсового транспортного средства обязан уступить дорогу встречным транспортным средствам и трамваю попутного направления дальше |
|Sphinx duration=30 | да вы и я же к рождеству равно к твому были заперты в бальном зале как это будет работать в двести тысяч в на нем взведённый взглядом в поэта приезжали в этом они бы смотреть на меня в рейхе воли говори признайтесь мне национальных попутного направления она товаров наверно она и на то вы не в порядке вернуться на трамвае товара таким образом були пересечения зарезать тебя да не оказалось товар обратно в замок разольется и лейтенанта наверно в окна в ноги и ликвидирована знали обязан егорова на трамвае в выздоровления в |


[Transcribing long audio files](https://cloud.google.com/speech-to-text/docs/async-recognize#speech_transcribe_async_gcs-python)

[Quickstart: Using client libraries](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries#client-libraries-usage-python)
