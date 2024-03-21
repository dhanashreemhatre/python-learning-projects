import sys
from cssmin import cssmin

def minify_css_file(input_file, output_file):
    with open(input_file, 'r') as f:
        css_code = f.read()

    minified_css = cssmin(css_code)

    with open(output_file, 'w') as f:
        f.write(minified_css)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python minify_css.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    minify_css_file(input_file, output_file)
