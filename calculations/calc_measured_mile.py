def calculate_productivity(df):

    df["Productivity"] = (
        df["Quantity"]
        / df["LabourHours"]
    )

    return df


def calculate_kpis(df):

    mm_productivity = df[
        df["Type"] == "MeasuredMile"
    ]["Productivity"].mean()

    impacted_productivity = df[
        df["Type"] == "Impacted"
    ]["Productivity"].mean()

    productivity_loss = (
        (
            mm_productivity
            - impacted_productivity
        )
        / mm_productivity
    ) * 100

    return {
        "mm_productivity": mm_productivity,
        "impacted_productivity": impacted_productivity,
        "productivity_loss": productivity_loss
    }