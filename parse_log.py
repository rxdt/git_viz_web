"""
This is a script to parse a text file that contains a commit log in pretty-format.
"""

from sys import argv
import re
import json

''' Creates a list named commits_list made up of dictionaries. 

The outer data structure is a list with a dictionary in each index.

Each inner dictionary represents one commit.
Each inner dictionary has possible keys of 'A', 'M', or 'D'.
Each inner dictionary's values are a list of the files that were Added, Modified, or deleted.
'''
def parse_log_to_dict(filename):
    commits_list = []
    pattern = re.compile('[A|D|M]\t')

    with open(filename, 'r') as f:
      for line in f:
        match = pattern.match(line)

        if line.startswith('commit '):
          single_commit = {}
          commits_list.append(single_commit)

        if match is not None:
          commit_process_key, commit_file_affected = line.split('\t', 1)

          if commit_process_key in single_commit:
            single_commit[commit_process_key].append(commit_file_affected.rstrip())
          else:
            single_commit[commit_process_key.strip()] = [commit_file_affected.rstrip()]

    f.close()

    return commits_list[::-1] # return list reversed with initial commit at index 0
    
    

def main():
    filename = '/Users/rxdt/log.txt'

    commits_list = parse_log_to_dict(filename)
    print commits_list

    with open('commits_json.txt', 'w') as outfile:
      outfile.write(unicode(json.dumps(commits_list, sort_keys=True, indent=2)))



if __name__ == "__main__":
    main()

