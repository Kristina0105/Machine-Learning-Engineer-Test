import camelot
import json

def extract_tables_from_pdf(pdf_path):
    tables_data = []

    try:
        tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')
    except Exception as e:
        print(f"Error extracting tables from PDF: {e}")
        return tables_data


    for index, table in enumerate(tables):
        table_data = {
            "tableName": f"Table {index + 1}",
            "columns": []
        }

        headers = table.df.columns.tolist()
        for header in headers:
            table_data["columns"].append({
                "header": header,
                "rows": table.df[header].tolist()
            })

        tables_data.append(table_data)

    return tables_data


def save_tables_to_json(tables_data, output_file):
    with open(output_file, 'w') as f:
        json.dump(tables_data, f, indent=4)

if __name__ == "__main__":
    pdf_path = "example.pdf" # Replace 'example.pdf' with the path to your PDF file
    output_file = "tables.json" # Name of the output JSON file

    tables_data = extract_tables_from_pdf(pdf_path)
    print("Extracted tables:", tables_data)
    save_tables_to_json(tables_data, output_file)
    print("Tables saved to JSON file:", output_file)