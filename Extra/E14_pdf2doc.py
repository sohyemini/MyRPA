import sys, os
from pdf2docx import parse

usage = """
[pdf2doc usage]
사용법은 다음과 같습니다.
pdf2doc input_pdf.pdf output_docx.docx
"""

if len(sys.argv) != 3:
    print(usage)
    exit(0)

pdf_file = sys.argv[1]
docx_file = sys.argv[2]
print(sys.argv)

if False == os.path.isfile(pdf_file):
    print(f"{pdf_file}이 존재하지 않습니다.")
    exit(0)

# 파일명과 확장자 분리
filename, ext = os.path.splitext(pdf_file)
print(ext)
if ext != '.pdf' and ext != '.PDF':
    print(f"PDF 파일을 입력으로 넣어주세요.")
    exit(0)

try:
    # convert pdf to docx
    parse(pdf_file, docx_file)
except:
    print("알 수 없는 에러가 발생했습니다")
