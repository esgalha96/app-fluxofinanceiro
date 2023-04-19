from django.http import HttpResponse
from datetime import datetime as dt
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.platypus import Image, SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY,TA_LEFT,TA_RIGHT
from reportlab.lib.styles import getSampleStyleSheet

class ReportBase():
    def __init__(self, request, report_title, path_logo):

        self.report_title = report_title
        self.request = request
        self.path_logo = path_logo
        
    def report_table(self, list_columns, list_dados, col_width):

        self.list_columns = list_columns
        self.list_dados = list_dados
        self.col_width = col_width
    
        PAGE_MARGIN = 3*cm
        report_title = self.report_title
        file_name = f'{report_title.lower()}_{dt.now().strftime(f"%Y%m%d_%H%M%S")}.pdf'.replace(' ','_')

        # Criar um objeto PDF usando SimpleDocTemplate
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
        doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=PAGE_MARGIN, leftMargin=PAGE_MARGIN, topMargin=PAGE_MARGIN, bottomMargin=PAGE_MARGIN)

        # Criar uma lista de elementos para serem adicionados ao PDF
        elements = []

        # Defina o estilo do título
        titulo_style = getSampleStyleSheet()['Title']
        titulo_style.alignment = TA_CENTER
        titulo_style.fontSize = 24
        titulo_style.spaceAfter = 12
        titulo_style.spaceBefore = 0

        # Crie uma tabela com 2 colunas
        table_data = [
            [Paragraph(report_title, titulo_style),Image(self.path_logo, width=50, height=50)],
        ]

        # Defina o estilo da tabela
        table_style = TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'RIGHT'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('FONTSIZE', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ])

        # Crie a tabela
        table = Table(table_data, colWidths=[None, 50*mm])
        table.setStyle(table_style)

        # Adicione a tabela ao documento
        elements.append(table)

        # Adicionar a tabela de dados
        table_style = [('ALIGN', (0,0), (-1,-1), 'CENTER'),
                        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0,0), (-1,0), 14),
                        ('BOTTOMPADDING', (0,0), (-1,0), 12),
                        ('GRID', (0,0), (-1,-1), 1, colors.gray)]

        row_styles = []
        for i, row in enumerate(self.list_dados):
            if i % 2 == 0:
                bg_color = colors.white
            else:
                bg_color = colors.lightgrey

            row_styles.append(('BACKGROUND', (0,i+1), (-1,i+1), bg_color))
            row_styles.append(('TEXTCOLOR', (0,i+1), (-1,i+1), colors.black))

        table_style.extend(row_styles)

        table_style = TableStyle(table_style)
        
        table = Table([self.list_columns] + self.list_dados, colWidths=self.col_width)
        table.setStyle(table_style)
        elements.append(table)
        
        doc.build(elements)
        return response