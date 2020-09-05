#!./env/bin/python
import os
import os.path
import jinja2
import argparse
from datetime import date

parser = argparse.ArgumentParser()
parser.add_argument('--title')
parser.add_argument('--category')

args = parser.parse_args()

print(args)

today = date.today()
today_str = date.isoformat(today)

template = jinja2.Template(
"""Title: {{ title }}
Date: {{ date }}
Category: {{ category }}
Tags:
Description:
""")

file_stub = template.render(title=args.title, date=today_str, category=args.category)

filepath = 'content/articles/' + args.category.lower() + '/' + args.title.replace(' ', '_').lower() + '.md'

# Make sure the folder exists
if not os.path.isdir('content/articles/' + args.category.lower()) :
    os.mkdir('content/articles/' + args.category.lower())

# Write file
with open(filepath, 'w') as OUTFILE:
    OUTFILE.write(file_stub)
