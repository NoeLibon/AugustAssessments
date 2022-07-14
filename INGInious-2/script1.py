import argparse

parser = argparse.ArgumentParser()
parser.add_argument('integers', nargs='+', type=int, help='les entiers à additionner')

args = parser.parse_args()

if __name__ == '__main__':
    print(sum(args.integers))
