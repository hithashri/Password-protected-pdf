import pikepdf

old_pdf=pikepdf.Pdf.open("try.pdf")

no_extract=pikepdf.Permissions(extract=False)

old_pdf.save("pro_new.pdf",
              encryption=pikepdf.Encryption(user="123asd",owner="hitha",allow=no_extract))
