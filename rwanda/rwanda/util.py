import os

import frappe
import pandas as pd


def import_villages():
    # Replace 'your_file.csv' with the actual path to your CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), "cells_per_bnr.csv")

    # Define the header based on your provided information
    csv_header = [
        "village_code",
        "village_name",
        "cell_code",
        "cell_name",
        "sector_code",
        "sector_name",
        "district_code",
        "district_name",
        "province_code",
        "province_name",
    ]

    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path, header=None, names=csv_header, skiprows=1)

        # Display the DataFrame (optional)
        print(df)

        for _, row in df.iterrows():
            province_code = create_or_get(
                "Province",
                {
                    "province_code": row["province_code"],
                    "province_name": row["province_name"],
                },
                row["province_code"],
            )

            district_code = create_or_get(
                "District",
                {
                    "province_code": province_code,
                    "district_code": row["district_code"],
                    "district_name": row["district_name"],
                },
                row["district_code"],
            )

            sector_code = create_or_get(
                "Sector",
                {
                    "province_code": province_code,
                    "district_code": district_code,
                    "sector_code": row["sector_code"],
                    "sector_name": row["sector_name"],
                },
                row["sector_code"],
            )

            cell_code = create_or_get(
                "Cell",
                {
                    "province_code": province_code,
                    "district_code": district_code,
                    "sector_code": sector_code,
                    "cell_code": row["cell_code"],
                    "cell_name": row["cell_name"],
                },
                row["cell_code"],
            )

            create_or_get(
                "Village",
                {
                    "province_code": province_code,
                    "district_code": district_code,
                    "sector_code": sector_code,
                    "cell_code": cell_code,
                    "village_code": row["village_code"],
                    "village_name": row["village_name"],
                },
                row["village_code"],
            )

        print("Data populated successfully.")

    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_file_path}' is empty.")
    except pd.errors.ParserError:
        print(
            f"Error: Unable to parse the CSV file '{csv_file_path}'. Check the file format."
        )
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def create_or_get(doc_type, filters, name):
    if frappe.db.exists(doc_type, name, cache=True):
        existing_doc = frappe.get_doc(doc_type, name)
        return existing_doc.name
    else:
        new_doc = frappe.get_doc({"doctype": doc_type, "name": name, **filters})
        new_doc.db_insert(ignore_if_duplicate=True)
        frappe.db.commit()
        return new_doc.name
