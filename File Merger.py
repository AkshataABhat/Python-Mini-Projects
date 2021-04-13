from PyPDF2 import PdfFileReader, PdfFileMerger
pdf_file1=PdfFileReader("file1.pdf")
pdf_file2=PdfFileReader("file2.pdf")
output=PdfFileMerger()
output.append(pdf_file1)
output.append(pdf_file2)
output.write("This_Is_The_Merged_File.pdf")
