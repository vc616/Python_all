# _*_ coding:utf-8 _*_
# fitz pymupdf ver =1.18.14
# Python 3.7
# 2021-11-17
# by gingeer @ CSDN
# 按位置获取发票信息并改名
# pymupdf doc see https://pymupdf.readthedocs.io/en/latest/

## make a new pdf with same size of old one.
##doc = fitz.open("some.file")
##page = doc[0]
##paths = page.get_drawings()  # extract existing drawings
### this is a list of "paths", which can directly be drawn again using Shape
### -------------------------------------------------------------------------
###
### define some output page with the same dimensions
##outpdf = fitz.open()
##outpage = outpdf.new_page(width=page.rect.width, height=page.rect.height)
##shape = outpage.new_shape()  # make a drawing canvas for the output page

import sys
import fitz
import re
import os, math
import datetime
# pip install pyMuPDF not fitz!!!!!!!!!!!!!
def make_text(words):
    """Return textstring output of get_text("words").
    Word items are sorted for reading sequence left to right,
    top to bottom.
    """
    line_dict = {}  # key: vertical coordinate, value: list of words
    words.sort(key=lambda w: w[0])  # sort by horizontal coordinate
    for w in words:  # fill the line dictionary
        y1 = round(w[3], 1)  # bottom of a word: don't be too picky!
        word = w[4]  # the text of the word
        line = line_dict.get(y1, [])  # read current line content
        line.append(word)  # append new word
        line_dict[y1] = line  # write back to dict
    lines = list(line_dict.items())
    lines.sort()  # sort vertically
    lines_2=[" ".join(line[1]) for line in lines]
   
    return lines_2
##    return "\n".join(lines_2)  #原方法



pdfPath='J:\\Users\\vc\\Desktop\\fp'
pagesfiles=[]
newnames=[]
files = os.listdir(pdfPath)

pdffiles = [f for f in files if f.lower().endswith('.pdf')]
print(pdffiles)

#大区域按百分比划分
invoice_rect_per = [0.69,0.02,0.978,0.2]
buyer_rect_per = [0.16,0.214, 0.57,0.369]
seller_rect_per = [0.16,0.744, 0.57,0.884]
total_amounts_per =[0.666,0.692, 0.95,0.749] 

for pdffile in pdffiles:

    # print(pdffile)
    doc = fitz.open(pdfPath+"\\"+pdffile)
    page = doc[0]
##    print(page)
    x_end=page.rect[2]
    y_end=page.rect[3]
    shape=page.new_shape()
##    print(x_end,y_end,page.rect)
    shape.draw_rect(page.rect)
    words = page.get_text("words")  # list of words on page
    
    ##===debug===
##    for word in words:
##        print(word[0]/x_end,word[1]/y_end,word[2]/x_end,word[3]/y_end,word[4])
##        print(word)
##        text_point=fitz.Point(word[0],word[3])
##        shape.draw_circle(text_point,1)
##        shape.insertText(text_point,word[4],color=(1,0,0),fontsize=8)
    #===debug end===


    invoive_rect = fitz.Rect(invoice_rect_per[0] * x_end,invoice_rect_per[1] * y_end, invoice_rect_per[2] * x_end,invoice_rect_per[3] * y_end)
    buyer_rect = fitz.Rect(buyer_rect_per[0] * x_end,buyer_rect_per[1] * y_end,buyer_rect_per[2] * x_end,buyer_rect_per[3] * y_end)
    seller_rect = fitz.Rect(seller_rect_per[0] * x_end,seller_rect_per[1] * y_end,seller_rect_per[2] * x_end,seller_rect_per[3] * y_end)
    total_amounts_rect = fitz.Rect(total_amounts_per[0] * x_end,total_amounts_per[1] * y_end,total_amounts_per[2] * x_end,total_amounts_per[3] * y_end)
    
    shape.draw_rect(total_amounts_rect) ## check positions


    #-----获取重要信息-------

    #----发票信息
    mywords_1 = [w for w in words if fitz.Rect(w[:4]) in invoive_rect]
    mywords_2 = [w for w in words if fitz.Rect(w[:4]).intersects(invoive_rect)]
    
    invoice_infos = make_text(mywords_1)
    check_invoice=False
    for info in invoice_infos:
        if re.search('\d{12}',info) != None:
            invoice_cata = info
            check_invoice=True
        elif re.search('\d{8}',info) != None:
            invoice_num = info
            check_invoice=True
        elif re.search('(\d{4})\D+(\d{2})\D+(\d{2})',info) !=None:
            date_re_result=re.search('(\d{4})\D+(\d{2})\D+(\d{2})',info)
            invoice_date='-'.join([date_re_result.group(1),date_re_result.group(2),date_re_result.group(3)])
            check_invoice=True
    if not check_invoice:
        print('不是发票文件',invoice_infos)
            # ===debug===
##        shape.finish(width=0.5,color=(1,0,0))
##        shape.commit()
##        doc.save('xjj.pdf')
##        doc.close()
##        dpi=200
##        zoom_x = dpi/72
##        zoom_y = dpi/72
##        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(0)
##        pix = page.getPixmap(matrix=mat, alpha=False)
##        pix.set_dpi(dpi,dpi)
##        pix.writePNG(pdffile + '.png')
    # ===debug end===
        continue
    else:
        invoice_num=invoice_num.replace('发票号码','')
        invoice_num=invoice_num.replace('：','')
        invoice_num=invoice_num.replace(':','')
        invoice_num=invoice_num.strip()

    #----购方
    buyer_words = [w for w in words if fitz.Rect(w[:4]) in buyer_rect]
    buyer_infos = make_text(buyer_words)
    for info in buyer_infos:
        if info.find('公司') >= 0:
            buyer=info
            break
        elif info =='个人':
            buyer='个人'

    #----卖方
    seller_words = [w for w in words if fitz.Rect(w[:4]) in seller_rect]
    seller_infos = make_text(seller_words)
    for info in seller_infos:
        if len(info) >3:
            seller=info
            break
                    


    #----合计金额
    total_amount_words = [w for w in words if fitz.Rect(w[:4]) in total_amounts_rect]
    total_amount_infos = make_text(total_amount_words)
    total_amount=total_amount_infos[-1]
    total_amount=total_amount.replace('¥','')
    total_amount=total_amount.replace('￥','')
    
    

    #----新名字    
    connector='_'
    # newname_elements=[invoice_date,invoice_num,buyer+'(购)',seller,'￥'+total_amount]
    newname_elements=[invoice_num,'￥'+total_amount]
    newname=connector.join(newname_elements) + '.pdf'

    


    
##    doc.save(pdffile)
    

        
    if newname == pdffile:
        print('发票名已经正规化！')
        newnames.append(newname)
        doc.close()
        print('------------------------')
        continue
        
    if newname not in newnames and newname not in pdffiles:
        print(f'原名：{pdffile}\n新名：{newname}')
        newnames.append(newname)
        doc.close()
        os.rename(pdfPath+"\\"+pdffile,pdfPath+"\\"+newname)
    else:
        
        while newname in newnames:
            newname = '_'+newname
    
        newnames.append(newname)
        doc.close()
        os.rename(pdffile,'_'+newname)
        print('重复文件名!已加前缀')
    
    print('------------------------')
    # ===debug===
##    shape.finish(width=0.5,color=(1,0,0))
##    shape.commit()
##    dpi=200
##    zoom_x = dpi/72
##    zoom_y = dpi/72
##    mat = fitz.Matrix(zoom_x, zoom_y).preRotate(0)
##    pix = page.getPixmap(matrix=mat, alpha=False)
##    pix.set_dpi(dpi,dpi)
##    pix.writePNG(pdffile + '.png')
    # ===debug end===
    
#    print(newname)
