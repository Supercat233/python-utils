import codecs

def convert_encoding(file_path, src='shift_jis', dst='utf-8'):
    with codecs.open(file_path, 'r', src) as f:
        content = f.read()
    with codecs.open(file_path, 'w', dst) as f:
        f.write(content)
    print(f"Converted encoding of {file_path} to {dst}")
