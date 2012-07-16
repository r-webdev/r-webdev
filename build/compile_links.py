#!/usr/bin/python
import re
import os
import sys
def get_html_filename(match):
  return "./"+match.replace(" ","_")+".html"

def get_markup_filename(match):
  return "./"+match.replace(" ","_")+".md"

def does_file_exist(filename):
  return os.path.exists(filename)

for line in sys.stdin:
  matches = re.split("\[\[(.*?)\]\]", line)
  for x,n in ( (matches[n], n ) for n in xrange(len(matches)) ):
    if n % 2 == 1:
      match = matches[n]
      html_filename = get_html_filename(match)
      html_classes = []
      if not does_file_exist(get_markup_filename(match)):
        html_classes.append("error404")

      match = """<a class="{html_class}" href="{html_filename}">{match}</a>""".format(html_filename=html_filename, match=match, html_class=" ".join(html_classes))
      matches[n] = match
  sys.stdout.write( ''.join(matches) )

