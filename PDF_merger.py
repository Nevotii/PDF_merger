#!/usr/bin/env python
# coding: utf-8

# In[3]:


# %load PDF_merger.py
#!/usr/bin/env python

# In[14]:


from PyPDF2 import PdfFileMerger
import os
import re

end = True
while end:
    pdfs = [i for i in os.listdir() if re.search('\.pdf$', i)]
    print(len(pdfs), pdfs)

    new_pdf = []
    for i in range(len(pdfs)):
        print(f'{pdfs[i]} position in the document is:')
        order = int(input())-1
        if (order == str or order > len(pdfs)):
            raise Exception('Stupid give the correct order')
        new_pdf.append(pdfs[order])
    print(f'The final order is:\n{new_pdf}')
    print('Do you want to proceed? y/n')
    if input() == 'y': 
        end = False
    else: 
        print('Choose the right order this time...')


merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)
    
print('Name of the new file?')
name = input() + '.pdf'
if len(name) == 4: 
    name = 'merged.pdf'
merger.write(name)
merger.close()

print('Your PDF has been successfully merged')

