import re


with open('certchain.pem', 'rt') as sourceFile:
    sourceFileContents = sourceFile.read()

print(re.sub(r'\n\n', '\n', sourceFileContents))
