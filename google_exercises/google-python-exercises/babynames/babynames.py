#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename, "r")
  html_text = f.read().split("\n")

  year_list = []
  all_names = []
  
  for x in html_text:
      year_pattern = re.search('Popularity\sin\s(\d{4})', x)
      name_rank_pattern = re.search('<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', x)
      if year_pattern:
          year = year_pattern.group(1)
          year_list.append(year)
      elif name_rank_pattern:
          line = [name_rank_pattern.group(1),name_rank_pattern.group(2),name_rank_pattern.group(3)]
          year_list.append(line)
  names_ranks = year_list[1:]
  rank_dict = {}
  ranks = []
  names = []
  
  for i in names_ranks:
      ranks.append(i[0])
      nm = [i[1],i[2]]
      names.append(nm)
      all_names.extend(nm)
      
  rank_dict = dict(zip(ranks, names))
  all_names.sort()
  
  result = [year_list[0]]
  
  for rn in all_names:
      for i, j in rank_dict.items():
          if rn in j:
              rn_string = rn+" "+i
              # line = "\n"+ rn_string
              result.append(rn_string)
  return result


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
  for x in args:
    summary_filename = x+".summary"
    f = open(summary_filename, "w")
    extract = extract_names(x)
    for y in extract:
      f.write(y+"\n")
    f.close()
  
if __name__ == '__main__':
  main()
