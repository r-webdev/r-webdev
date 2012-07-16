#!/usr/bin/python
import re
import os
import sys

def clean_human(cleanme):
  ret = cleanme.replace("_"," ")
  return ret

def clean_filesystem(cleanme):
  ret = cleanme.replace(" ","_")
  return ret

 
def get_html_filename(match):
  return "./"+match.replace(" ","_")+".html"

def get_markup_filename(match):
  return "./"+match.replace(" ","_")+".md"

def does_file_exist(filename):
  return os.path.exists(filename)


def get_link(match):
  html_filename = get_html_filename(match)
  html_classes = []
  human_match = clean_human(match)
  if not does_file_exist(get_markup_filename(match)):
    html_classes.append("error404")
    return """<a class="{html_class}" href="./404.html#{match}md">{human_match}</a>""".format(human_match=human_match, html_filename=html_filename, match=match, html_class=" ".join(html_classes))
  else: 
    return """<a class="{html_class}" href="{html_filename}">{human_match}</a>""".format(human_match=human_match, html_filename=html_filename, match=match, html_class=" ".join(html_classes))

print "#%s" % clean_human(sys.argv[1])
for line in sys.stdin:
  matches = re.split("\[\[(.*?)\]\]", line)
  for x,n in ( (matches[n], n ) for n in xrange(len(matches)) ):
    if n % 2 == 1:
      match = matches[n]
      matches[n] = get_link(match)
  sys.stdout.write( ''.join(matches) )

