#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
@author: yueyao
@file: create_rnadenovo_pdf.py
@time: 2018/10/19
'''


import sys
import os
import re
import subprocess
import configparser
import glob
from optparse import OptionParser

sep_str=os.sep   ###显示不同系统分隔符

intro='''
    测序流程
'''
# print( sep_str)
# print(intro)


tex_start='''\\documentclass[10pt, oneside,a4paper]{article}
\\usepackage[text={170mm, 230mm}, vmarginratio=1:1]{geometry}
\\usepackage[slantfont,boldfont]{xeCJK}
\\setCJKmainfont{WenQuanYi Zen Hei}
\\usepackage{array}
\\usepackage{tabularx}
\\usepackage[colorlinks, linkcolor=black, anchorcolor=blue, citecolor=green]{hyperref}
\\usepackage{upgreek}
\\usepackage{xcolor, color}
\\usepackage[framemethod=tikz]{mdframed}
\\usepackage{graphicx, psfrag}
\\usepackage{fancyhdr}
\\pagestyle{fancy}
\\usepackage{indentfirst}
\\setlength{\\parindent}{2em}
\\setlength{\\headheight}{30 pt}
\\lhead{}
\\chead{\\includegraphics[width=140 mm, keepaspectratio]{%(yemei)s}}
\\rhead{}
\\lfoot{}
\\cfoot{\\thepage}
\\rfoot{}
\\我的生活(hha)%(renminbi)s
'''
haha="haha,woshi shui "
rmb='.\sss/xxx'
tex_start = tex_start %{'yemei':haha,'renminbi':rmb}
# print(tex_start)

# os.system('del xxx.txt')

table_tail='''
\\hline
\\end{tabular}
\\begin{tablenotes}
\\item[1]Q20: 质量值大于20的碱基数目占总碱基数目的比例.\\par
\\item[1]Total Clean Reads(Mb)： 过滤后的reads数\\par
\\item[2]Total Clean Bases(Gb)： 过滤后的碱基总数\\par
\\item[3]Clean Reads Q20(\\%)： 过滤后的reads中质量值大于20的碱基数占总碱基数的百分比\\par
\\item[4]Clean Reads Q30(\\%)： 过滤后的reads中质量值大于30的碱基数占总碱基数的百分比\\par
\\item[5]Clean Reads Ratio(\\%)： 过滤后的reads的比例\\par
\\end{tablenotes}
\\end{threeparttable}}
\\end{table}
\\begin{figure}[H]
\\centering
\\includegraphics[width = 0.6\\textwidth,keepaspectratio]{%(filter_base)s}
\\par
\\caption{Clean reads的碱基含量分布图。X轴代表碱基在read中的位置， Y轴代表此类碱基的含量比例。 正常情况下， reads每个位置的碱基含量分布稳定， 无AT或GC分离现象。由于
Illumina平台在RNA-Seq测序中， 反转录成cDNA时所用的6bp随机引物会引起前6个位置的GC含量组成存在偏好性， 故图中前6bp的波动为正常现象。}
\\label{ReadsHeatmap}
\\end{figure}
\\vspace{5 mm}

\\begin{figure}[H]
\\centering
\\includegraphics[width = 0.6\\textwidth,keepaspectratio]{%(filter_qual)s}
\\par
\\caption{X轴代表碱基在read中的位置，Y轴代表碱基质量值，图中每个点表示此位置达到某一质量值的碱基总数，颜色越深表示数目越多。
碱基质量分布反映了测序reads的准确性，测序仪、测序试剂、样品质量等均能影响碱基质量。正常情况下，reads中的前几个碱基质量值不高，
是因为反转录时随机引物不能很好地结合RNA模板；随着测序长度的增加，高质量碱基的比例会有所提高；但长度达到一定阈值后，
由于测序试剂的消耗，高质量碱基的比例会降低。从整体上看，如果低质量(Quality<20)的碱基比例较低， 说明测序质量较好}
\\label{ReadsHeatmap}
\\end{figure}
\\vspace{5 mm}

'''

a='.\BGI_result/1.CleanData/EUlefqual.png'
b='.\BGI_result/1.CleanData/EUlefqual.png'
# table_tail=table_tail%{'filter_qual':"a",'filter_base':"b"}

# print(table_tail)

abc='''
\\includegraphics[width = 0.6\\textwidth,keepaspectratio]{%(filter_base)s}
\\includegraphics[width = 0.6\\textwidth,keepaspectratio]{%(filter_qual)s}
\\caption{X轴代表碱基在read中的位置，Y轴代表碱基质量值，图中每个点表示此位置达到某一质量值的碱基总数，颜色越深表示数目越多。
碱基质量分布反映了测序reads的准确性，测序仪、测序试剂、样品质量等均能影响碱基质量。正常情况下，reads中的前几个碱基质量值不高，
是因为反转录时随机引物不能很好地结合RNA模板；随着测序长度的增加，高质量碱基的比例会有所提高；但长度达到一定阈值后，
由于测序试剂的消耗，高质量碱基的比例会降低。从整体上看，如果低质量(Quality<20)的碱基比例较低， 说明测序质量较好}
'''
abc=abc % {'filter_qual':a,'filter_base':b}
print(abc)