from pathlib import Path
path = Path('python/pi_million_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)