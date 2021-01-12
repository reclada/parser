import csv
import json
import sys


def make_cells(rownum, row):
    return [
        {
            "bbox": [colnum, rownum, colnum + 1, rownum + 1],
            "text": text
        }
        for colnum, text in enumerate(row)
    ]


def main():
    table = {
        "type": "table",
        "bbox": [0, 0, 1, 1],
        "rows": []
    }
    data = {
        "document": {
            "path": sys.argv[1],
            "pages": [
                {
                    "page_num": 0,
                    "blocks": [
                        table
                    ]
                }
            ]
        }
    }
    with open(sys.argv[1]) as f:
        if sys.argv[1].endswith(".txt") or sys.argv[1].endswith(".tsv"):
            dialect = csv.excel_tab
        else:
            dialect = csv.excel
        reader = csv.reader(f, dialect=dialect)
        table["header"] = make_cells(0, next(reader))
        for rownum, row in enumerate(reader):
            table["rows"].append({"cells": make_cells(rownum + 1, row)})

    with open(sys.argv[2], "w") as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()
