import sys
import markdown

with open(sys.argv[2], 'r') as input_file:
    contents = input_file.read()
    html = markdown.markdown(contents)

with open(sys.argv[3], 'w') as output_file:
    output_file.write(html)