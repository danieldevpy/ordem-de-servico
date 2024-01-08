from fpdf import FPDF
import base64
import json
from src.domain.entity.order import Order

class GeneratePdfHTML:

    @classmethod
    def generate(cls, order: Order = None) -> str:
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('ArialUnicodeMS', '', 'unicode.ttf', uni=True)
        pdf.set_font("Arial", size=12)

        line_height = pdf.font_size * 2.5

        _json = order.data_json.replace("'", '"')
        data_json = json.loads(_json)

        for titulo in data_json:
            pdf.set_fill_color(245, 245, 245)
            pdf.set_text_color(0, 0, 0)
            pdf.set_font("Arial", "B", size=16)
            pdf.cell(0, line_height, titulo.upper(), ln=True, align="L", fill=True)
            
            for field in data_json[titulo]:
                pdf.set_fill_color(255, 255, 255)
                pdf.set_text_color(50, 50, 50)
                pdf.set_font("Arial", "B", size=12)
                pdf.multi_cell(pdf.w//2.6, line_height, field.upper(), border=1, align="CENTER",
                        new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size*10, fill=True)
                pdf.set_font("ArialUnicodeMS", size=12)
                try:
                    value = data_json[titulo][field]
                    if type(value) == list:
                        aux = ""
                        for item in value:
                            aux = aux + " " + item + ","
                        value = aux[:-1]
                
                    pdf.multi_cell(pdf.w//1.9, line_height, value.upper(), border=1, align="CENTER",
                        new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size*10, fill=True)
                    
                    if len(value) > 100:
                        pdf.ln(line_height + (len(value)//2))
                        
                except:
                    pdf.multi_cell(pdf.w//2.2, line_height, "error", border=1, align="CENTER",
                        new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size, fill=True)
                    

                pdf.ln(line_height)
            pdf.ln(line_height+5)

        pdf_output = pdf.output(dest='S')  # Directly get the bytearray output
        
        # Codificando o conteúdo do PDF em base64
        pdf_base64 = base64.b64encode(pdf_output).decode()

        # Criando o HTML para exibir o PDF no QWebEngineView
        html = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="100%" height="100%"></iframe>'

        return html, pdf_output
