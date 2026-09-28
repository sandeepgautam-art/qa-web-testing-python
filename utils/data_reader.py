"""Reads rows from test-data/test_data.csv."""
import csv
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "test-data" / "test_data.csv"


def get_test_data(data_id):
    """Return one CSV row (as a dict) whose data_id matches.

    Empty cells come back as empty strings, which is exactly what we want
    when a test needs to leave a field blank.
    """
    with open(DATA_FILE, newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            if row["data_id"] == data_id:
                return row
    raise KeyError(f"No test data found for data_id='{data_id}' in {DATA_FILE}")
