import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="guest")
parser.add_argument("--age", default="unknown")
parser.add_argument("--city", default="nowhere")
parser.add_argument("-h")
args = parser.parse_args()

if args.h:
    print("Скрипт приймає аргументи для імені користувача (name), віку (age) та міста (city), щоб вивести персоналізоване привітання, введіть в термінал, наприклад --name 'Milena' і тд")
print(f"Hi, {args.name}! You're {args.age} years old and you live in {args.city}")


