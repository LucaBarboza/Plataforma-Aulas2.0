import sys

def main():
    try:
        import pypdf
        print("Using pypdf")
        reader = pypdf.PdfReader("matd38_-_estatistica_basica_b.pdf")
        for i, page in enumerate(reader.pages):
            print(f"--- PAGE {i+1} ---")
            print(page.extract_text())
        return
    except ImportError:
        pass

    try:
        import PyPDF2
        print("Using PyPDF2")
        reader = PyPDF2.PdfReader("matd38_-_estatistica_basica_b.pdf")
        for i, page in enumerate(reader.pages):
            print(f"--- PAGE {i+1} ---")
            print(page.extract_text())
        return
    except ImportError:
        pass

    try:
        import pdfplumber
        print("Using pdfplumber")
        with pdfplumber.open("matd38_-_estatistica_basica_b.pdf") as pdf:
            for i, page in enumerate(pdf.pages):
                print(f"--- PAGE {i+1} ---")
                print(page.extract_text())
        return
    except ImportError:
        pass

    print("No PDF extraction library found. Attempting to install pypdf...")

if __name__ == "__main__":
    main()
