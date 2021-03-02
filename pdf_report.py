
from fpdf import FPDF
   



# save FPDF() class into  
# a variable pdf 
pdf = FPDF()    
   
# Add a page 
pdf.add_page() 
pdf.accept_page_break()  
# set style and size of font  
# that you want in the pdf 
pdf.set_font("Arial", size = 10) 


# open the text file in read mode 

f = open("fourier_transform_log.txt", "r") 
  
# insert the texts in pdf 


line_count = 1

w_img = 150
h_img = 100

h_line = 5
h_text = 10
line_inc = 1

for x in f:

    if 'save plot' in x:
        
        #change page, if image is too large
        
        img_path = x.split(' -> ')[1]
        print(pdf.get_y())
        pdf.cell(200, h_line, txt = '', ln = line_inc, align = 'L')
        line_inc = h_img/h_line
        pdf.cell(200, h_line, txt = '', ln = line_inc, align = 'L')
        y_img = pdf.get_y()
        pdf.image(img_path[:-1], 10, y_img, w_img, h_img, type='jpg') 
        line_inc = 1
        
        print('plot, line count: '+str(line_count))
    else:
        print('text only, line count: '+str(line_count))
        #pdf.text(0, line_count*h_text, txt = x)
        
        pdf.cell(200, h_line, txt = x, ln = line_inc, align = 'L')
        line_inc = 1
