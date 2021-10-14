from posix import listdir
from posixpath import dirname
import img2pdf
import sys
import os
from fpdf import FPDF



if len(sys.argv) != 2:
    print("digite o caminho da pasta onde estão as imagens")


if ('output.pdf' in os.listdir(os.getcwd())):
    print(listdir(os.getcwd()))
    os.remove('output.pdf')


pdf = FPDF('P', 'mm', 'A4')
pdf.add_page('P')
pdf.output('output.pdf', 'F')

dirname = sys.argv[1]
imgs = []
for fname in os.listdir(dirname):
	path = os.path.join(dirname, fname)
	if os.path.isdir(path):
		continue
	imgs.append(path)



with open("output.pdf","wb") as f:
	f.write(img2pdf.convert(imgs))


