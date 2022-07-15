import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', nargs='?')
parser.add_argument('--output_file', nargs='?')
parser.add_argument('--filter_teacher', nargs='?')
parser.add_argument('--filter_good', nargs='?')
parser.add_argument('--order', action='store_true')
parser.add_argument('--select', nargs='?')

args = parser.parse_args()

rf = open(args.input_file, 'r')
json_content = rf.read()
rf.close()
grades = json.loads(json_content)

i = 0
while i < len(grades):
    if not args.filter_teacher:
        break
    if grades[i]['Teacher'] != args.filter_teacher:
        del grades[i]
        i -= 1
    i += 1

i = 0
while i < len(grades):
    if not args.filter_good:
        break
    if float(grades[i]['Grade']) < float(args.filter_good):
        del grades[i]
        i -= 1
    i += 1


def sort_by_name(x):
    return x['Name']


if args.order:
    grades.sort(key=sort_by_name)

i = 0
while i < len(grades):
    if not args.select:
        break
    selected_keys = args.select.split(',')
    all_keys = list(grades[i])
    for key in all_keys:
        if key not in selected_keys:
            del grades[i][key]
    i += 1

wf = open(args.output_file, 'w') if args.output_file else open(args.input_file, 'w')

if __name__ == '__main__':
    wf.write(json.dumps(grades, indent=2))
    wf.close()
