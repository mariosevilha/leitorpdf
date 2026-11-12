from PyPDF2 import PdfReader
import pandas
import pandas as pd

def mostrar_texto_numerado(caminho_pdf):
    reader = PdfReader(caminho_pdf)
    n = 1
    linhas = []
    for i, pagina in enumerate(reader.pages, start=1):
        print(f"--- Página {i} ---")
        texto = pagina.extract_text() or ""
        for linha in texto.splitlines():
            print (f"{n:03d}:{linha}")
            linhas.append(linha)
            n += 1
    return linhas

def salvar_informação(salvar):
    dados = []
    dados.append({
        "NF":salvar[1],
    })

    caminho_excel = r"C:\Users\pc\Downloads\resultado.xlsx"
    df = pd.DataFrame(dados)
    df.to_excel(caminho_excel, index=False)

linhas = mostrar_texto_numerado(r"C:\Users\pc\Downloads\Nova Pasta\nota-fiscal-notebook-dell.pdf")
salvar_informação(linhas)