from fpdf import FPDF
import pandas as pd
import random
from Assests.friend import *
from Assests.user import * 

'''
Generate report function 
'''


def generate_report(results, main_user):
    """
    Generates 
    :param scores:
    :param results:
    :param main_user:
    """
    # employ Series (pandas) to easily store and write data to pdf 
    s = pd.Series(list(results.values()), index = list(results.keys()))
    s = s.sort_values() 

    # setup the PDF page
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)

    # setup the title
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(75, 10, "Letterboxd Friend Ranker: Report for " + main_user.username +
             " | Lower the avg. difference, the more in common", 0, 2,
             'C')

    # setup the main table
    pdf.cell(90, 10, " ", 0, 1, 'C')
    pdf.cell(50, 10, 'User', 1, 0, 'C')
    pdf.cell(40, 10, 'Avg. Difference', 1, 1, 'C')
    pdf.set_font('arial', '', 12)

    # write the data to table
    for i, j in s.items():
        pdf.cell(50, 10, '%s' % (str(i)), 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(round(j, 2))), 1, 1, 'C')
   
    report_name = "Lbox_Ranker_Report_" + main_user.username + ".pdf"
    pdf.output(report_name, 'F')