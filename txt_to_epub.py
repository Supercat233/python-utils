from ebooklib import epub

def txt_to_epub(txt_path, output_name):
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    book = epub.EpubBook()
    book.set_identifier('id123456')
    book.set_title(output_name)
    book.set_language('en')

    chapter = epub.EpubHtml(title='Chapter 1', file_name='chap_1.xhtml', lang='en')
    chapter.content = f"<h1>{output_name}</h1><p>{content.replace('\\n', '<br>')}</p>"

    book.add_item(chapter)
    book.toc = (epub.Link('chap_1.xhtml', 'Chapter 1', 'chap_1'),)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ['nav', chapter]

    epub.write_epub(f"{output_name}.epub", book)
    print(f"EPUB created: {output_name}.epub")

if __name__ == "__main__":
    txt_path = input("Enter .txt file path: ")
    name = input("Enter output EPUB name: ")
    txt_to_epub(txt_path, name)
