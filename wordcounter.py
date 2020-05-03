import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Wordcounter')
    parser.add_argument("name", help= "Soubor pro čtení")
    parser.add_argument("--characters", help="Spočítá všechny znaky", action="store_true")
    parser.add_argument("--words", help="Spočítá všechna slova", action="store_true")
    parser.add_argument("--lines", help="Spočítá všechny řádky", action="store_true")

    args = parser.parse_args()

    try:
        soubor = open(args.name)
        text = soubor.read()

        if args.characters and args.words and args.lines:
            characters = len(text)
            lines = len(text.split("\n"))
            words = len(text.split(" ")) + (lines - 1)
            print(f"\n{text}\n\nCelkový počet znaků:{characters}, Celkový počet slov:{words}, Celkový počet řádků:{lines} \n")
            soubor.close()

        elif args.characters and args.words:
            characters = len(text)
            lines = len(text.split("\n"))
            words = len(text.split(" ")) + (lines - 1)
            print (f"\n{text}\n\nCelkový počet znaků:{characters}, Celkový počet slov: {words}\n")
            soubor.close()

        elif args.characters and args.lines:
            characters = len(text)
            lines = len(text.split("\n"))
            print (f"\n{text}\n\nCelkový počet znaků:{characters}, Celkový počet řádků:{lines}\n")
            soubor.close()

        elif args.words and args.lines:
            lines = len(text.split("\n"))
            words = len(text.split(" ")) + (lines - 1)
            print(f"\n{text}\n\nCelkový počet slov:{words}, Celkový počet řádků:{lines}\n")
            soubor.close()

        elif args.characters:
            characters = len(text)
            print(f"\n{text}\n\nCelkový počet znaků:{characters} \n")
            soubor.close()

        elif args.words:
            lines = len(text.split("\n"))
            words = len(text.split(" ")) + (lines - 1)
            print (f"\n{text}\n\nCelkový počet slov: {words} \n")
            soubor.close()

        elif args.lines:
            lines = len(text.split("\n"))
            print (f"\n{text}\n\nCelkový počet řádků:{lines}\n")
            soubor.close()

        else:
            characters = len(text)
            lines = len(text.split("\n"))
            words = len(text.split(" ")) + (lines - 1)
            print(f"\n{text}\n\nCelkový počet znaků:{characters}, Celkový počet slov:{words}, Celkový počet řádků:{lines}\n")
            soubor.close()

    except:
        print ("Chybný soubor.")
        sys.exit()
     main()





