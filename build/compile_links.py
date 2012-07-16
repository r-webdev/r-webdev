#!/usr/bin/python
import re
import sys
def get_html_filename(match):
  return "./"+match.replace(" ","_")+".html"
for line in sys.stdin:
  matches = re.split("\[\[(.*?)\]\]", line)
  for x,n in ( (matches[n], n ) for n in xrange(len(matches)) ):
    if n % 2 == 1:
      match = matches[n]
      html_filename = get_html_filename(match)
      match = """<a href="{html_filename}">{match}</a>""".format(html_filename=html_filename, match=match)
      matches[n] = match
  sys.stdout.write( ''.join(matches) )

