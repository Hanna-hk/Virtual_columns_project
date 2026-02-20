import pandas as pd
import re
def add_virtual_column(df: pd.DataFrame, role: str, new_column: str)->pd.DataFrame:
    """
    Creates a new DataFrame with an additional calculated column based on a mathematical expression.

    This function takes an existing pandas DataFrame and appends a 'virtual' column
    derived from operations (addition, subtraction, or multiplication) performed on
    existing columns. If the provided mathematical expression or any
    column labels are invalid, an empty DataFrame is returned.

    Args:
        df (pd.DataFrame): The source pandas DataFrame containing the original data.
        role (str): A mathematical expression defining the calculation (e.g.,
            'col_a + col_b'). Supports '+', '-', and '*' operators.
        new_column (str): The name assigned to the newly created virtual column.

    Returns:
        pd.DataFrame: A new DataFrame instance containing the original data and the
        calculated column.

    Validations:
        * Column labels must consist only of letters and underscores (_).
        * The expression must use supported operations: +, -, or *.
        * Returns an empty DataFrame if the expression or labels are incorrect.

    Example:
        >>> data = pd.DataFrame({'sales': [100, 200], 'costs': [40, 60]})
        >>> add_virtual_column(data, 'sales - costs', 'profit')
           sales  costs  profit
        0    100     40      60
        1    200     60     140
    """
    ## VALIDATION PART
    role = re.sub(r'\s+', '', role)
    ## Splitting the role based on operators
    elements = re.split(r'([*+-])', role)
    if (len(elements) != 3
            or not check_column(elements[0])
            or not check_column(elements[2])
            or not elements[0] in df.columns
            or not elements[2] in df.columns
            or not check_column(new_column)):
        return pd.DataFrame()

    ## CALCULATING PART
    new_df = df.copy(deep=True)
    column1 = elements[0]
    column2 = elements[2]
    operator = elements[1]
    match operator:
        case '+': new_df[new_column] = new_df[column1] + new_df[column2]
        case '-': new_df[new_column] = new_df[column1] - new_df[column2]
        case '*': new_df[new_column] = new_df[column1] * new_df[column2]
        case _: return pd.DataFrame()

    return new_df

def check_column(column: str)-> bool | None:
    """
    Checks whether a column label consists only of letters and underscores (_).
    :param column: str
    :return: bool
    """
    pattern = r"^[a-zA-Z_]+$"
    for s in column:
        if not re.match(pattern, s):
            return False
    return True