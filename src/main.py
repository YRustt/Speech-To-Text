import argparse

from settings import get_fullpath, get_denoise_filename
from methods import GoogleAdapter, SphinxAdapter, GoogleCloudAdapter
from denoise import denoise


def get_args():
    """Парсинг аргументов коммандной строки."""

    parser = argparse.ArgumentParser(description="Приложение для преобразования аудио в формате wav в текст.")

    subparsers = parser.add_subparsers(help="режимы работы", dest="subparser")

    recognize_parser = subparsers.add_parser("recognize", help="режим преобразования аудио в текст")
    recognize_parser.add_argument("-t", "--type", choices=["google", "sphinx", "google.cloud"], help="тип преобразователя", dest="type", required=True)
    recognize_parser.add_argument("-d", "--duration", help="длина промежутка в секундах", type=int, dest="duration", required=False)
    recognize_parser.add_argument("-u", "--uri", help="путь к файлу в бакете", dest="uri", required=False)
    recognize_parser.add_argument("-l", "--long", help="длительный запуск", action="store_true", dest="long", required=False)

    denoise_parser = subparsers.add_parser("denoise", help="режим удаления шума из аудио")

    parser.add_argument("-f", "--file", help="путь к файлу с аудио", dest="file", required=False)
    args = parser.parse_args()
    return args


def main():
    args = get_args()

    if args.subparser is None:
        return

    filename = args.file
    uri = args.uri
    long = args.long

    if args.subparser == "denoise":
        output_filename = get_denoise_filename(filename)
        denoise(filename, output_filename)

    if args.subparser == "recognize":
        if args.type == "google":
            adapter = GoogleAdapter() 
        elif args.type == "sphinx":
            adapter = SphinxAdapter()
        elif args.type == "google.cloud":
            adapter = GoogleCloudAdapter()
        
        duration = args.duration
        text = adapter.speech_to_text(filename=filename, duration=duration, uri=uri, long=long)
        print(text)


if __name__ == "__main__":
    main()
