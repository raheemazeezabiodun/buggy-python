"""
Simple python script to read a json file of loan
then add perform some calculations on the data
"""
from json import load


def read_file():
    with open('loans.json', 'r') as json_file:
        data = load(json_file)
        return data


def calculate_unpaid_loans(data):
    """
    Calculate unpaid loans

    :params :data -> dictionary (JSON Object)
    :return int
    """
    loans = data.get("loans")
    unpaid_loans = [loan.get("amount") for loan in loans if loan.get("status") == "unpaid"]
    return sum(unpaid_loans)


def get_paid_loans(data):
    """
    Get paid loans

    :params: data -> dictionary (JSON Object)
    :return list
    """
    loans = data.get("loans")
    return [loan.get("amount") for loan in loans if loan.get("status") == "paid"]

def calculate_paid_loans(data):
    """
    Calculate paid loans

    :params :data -> dictionary (JSON Object)
    :return int
    """
    return sum(get_paid_loans(data))


def average_paid_loans(data):
    """
    Calculate average paid loans

    :params :data -> dictionary (JSON Object)
    :return int
    """
    paid_loans = get_paid_loans(data)
    sum_paid_loans = sum(paid_loans)
    number_paid_loans = len(paid_loans)
    average = (sum_paid_loans / number_paid_loans)
    return average
