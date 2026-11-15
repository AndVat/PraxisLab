def validate_columns(df, required_columns):

    missing_columns = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    return missing_columns