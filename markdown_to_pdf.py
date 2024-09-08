import markdown
import pdfkit

def convert_md_to_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html = markdown.markdown(md_content)

    # 使用自定义样式（可选）
    html = f"<html><body>{html}</body></html>"

    pdfkit.from_string(html, pdf_path)
    print(f"✅ Converted to PDF: {pdf_path}")

if __name__ == "__main__":
    md_file = input("Enter path to .md file: ")
    pdf_file = input("Enter output PDF filename: ")
    convert_md_to_pdf(md_file, pdf_file)
