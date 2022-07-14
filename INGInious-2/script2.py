import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text_file', nargs='?')

args = parser.parse_args()

file = open(args.text_file, 'r')
text = file.read()
file.close()
split_text = text.split()


def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


numbers = []
for item in split_text:
    if isfloat(item):
        numbers.append(float(item)) if '.' in item else numbers.append(int(item))

if __name__ == '__main__':
    print(max(numbers))
