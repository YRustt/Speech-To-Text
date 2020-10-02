import argparse

from settings import get_fullpath, get_denoise_filename
from methods import GoogleAdapter, SphinxAdapter
from denoise import denoise


def get_args():
    """Парсинг аргументов коммандной строки."""

    parser = argparse.ArgumentParser(description="Приложение для преобразования аудио в формате wav в текст.")

    subparsers = parser.add_subparsers(help="режимы работы", dest="subparser")

    recognize_parser = subparsers.add_parser("recognize", help="режим преобразования аудио в текст")
    recognize_parser.add_argument("-t", "--type", choices=["google", "sphinx"], help="тип преобразователя", dest="type", required=True)
    recognize_parser.add_argument("-d", "--duration", help="длина промежутка в секундах", type=int, dest="duration", required=False)

    denoise_parser = subparsers.add_parser("denoise", help="режим удаления шума из аудио")
    
    parser.add_argument("-f", "--file", help="путь к файлу с аудио", dest="file", required=True)
    args = parser.parse_args()
    return args


def main():
    args = get_args()

    if args.subparser is None:
        return

    filename = args.file

    if args.subparser == "denoise":
        output_filename = get_denoise_filename(filename)
        denoise(filename, output_filename)

    if args.subparser == "recognize":
        if args.type == "google":
            adapter = GoogleAdapter() 
        elif args.type == "sphinx":
            adapter = SphinxAdapter()
        
        duration = args.duration
        text = adapter.speech_to_text(filename, duration)
        print(text)


if __name__ == "__main__":
    main()
