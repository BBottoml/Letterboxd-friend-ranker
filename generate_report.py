from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
import pandas as pd
import random

'''
Generate report function 
'''


def generate_report(scores, results, main_user):
    """

    :param scores:
    :param results:
    :param main_user:
    """
    df = pd.DataFrame()
    df['User'] = list(results.values())
    df['Scores'] = scores

    # setup the scatter plot
    title("Letterboxd Friend Ranker: Scatter Plot")
    xlabel('')
    ylabel('Score')

    c = [2.0, 4.0, 6.0, 8.0]
    m = [x - 0.5 for x in c]

    xticks(c, df['User'])

    bar(m, df['Mike'], width=0.5, color=rand_color(), label="Mike")
    bar(c, df['Charles'], width=0.5, color=rand_color(), label="Charles")

    legend()
    axis([0, 10, 0, 8])
    savefig('barchart.png')

    # setup the PDF page
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(75, 10, "Letterboxd Friend Ranker: Report for " + main_user.username +
             " | Lower the avg. difference, the more in common", 0, 2,
             'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-40)
    pdf.cell(50, 10, 'User', 1, 0, 'C')
    pdf.cell(40, 10, 'Charles', 1, 0, 'C')
    pdf.cell(40, 10, 'Mike', 1, 2, 'C')
    pdf.cell(-90)
    pdf.set_font('arial', '', 12)
    for i in range(0, len(df)):
        pdf.cell(50, 10, '%s' % (df['User'].iloc[i]), 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(df.Mike.iloc[i])), 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(df.Charles.iloc[i])), 1, 2, 'C')
        pdf.cell(-90)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-30)
    pdf.image('barchart.png', x=None, y=None, w=0, h=0, type='', link='')
    pdf.output('test.pdf', 'F')


def rand_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
