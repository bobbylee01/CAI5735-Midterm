# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.24.2",
#     "matplotlib>=3.8,<3.11",
#     "pandas==3.0.5",
#     "seaborn>=0.13,<0.14",
# ]
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    return mo, pd, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Diabetes Readmission Analysis
    ###Research Question: "*Among patients with diabetes is the number of diagnoses associated with length of stay and readmission* "
    ####Group 3: Bobby Lee, Arnold Obungu, Micheal LaBrie

    This notebook will examine three columns from the Diabetes 130-US Hospitals (1999-2008) dataset.
    - number_diagnoses
    - readmitted
    - time_in_hospital
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Display the CSV
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('diabetes_130.csv')
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###Number of Diagnoses
    """)
    return


@app.cell
def _(df):
    df['number_diagnoses'].describe()
    return


@app.cell
def _(df, plt, sns):
    plt.figure(figsize=(8,5))
    sns.histplot(data=df, x='number_diagnoses')
    plt.title('Distribution of Number of Diagnoses')
    plt.xlabel("Number of Diagnoses", fontsize=12)
    plt.ylabel("Encounters", fontsize=12)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ####The histogram shows that most common number of diagnoses among hospital encounters is 9.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###Types of Readmission
    - Not readmitted
    - within 30 days
    - after 30 days
    """)
    return


@app.cell
def _(df, plt, sns):
    plt.figure(figsize=(8,5))
    sns.histplot(data=df, x='readmitted', hue="readmitted")
    plt.title("Distribution of Readmission Status")
    plt.xlabel("Readmission Status", fontsize=12)
    plt.ylabel("Encounters", fontsize=12)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ####The histogram shows that most patients are not readmitted with those readmitted after 30 days being second most common, followed by readmission within 30 days.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###Number of Diagnoses vs Readmission
    """)
    return


@app.cell
def _(df, plt, sns):
    plt.figure(figsize=(8,5))
    sns.boxplot(data=df, x='number_diagnoses', y='readmitted', hue="readmitted")
    plt.title('Number of Diagnoses vs Readmission')
    plt.xlabel("Readmission Status", fontsize=12)
    plt.ylabel("Number of Diagnoses", fontsize=12)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ####The box plot shows that patients readmitted after 30 days had the highest median number of diagnoses at 9, compared to 8 for those readmitted within 30 days and those not readmitted.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Time Patients Spent Inside the Hospital
    """)
    return


@app.cell
def _(df):
    df['time_in_hospital'].describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###Time in Hospital vs Readmission
    """)
    return


@app.cell
def _(df, plt, sns):
    sns.boxplot(data=df, x='time_in_hospital', y='readmitted', hue="readmitted")
    plt.xlabel("Time in Hospital")
    plt.ylabel("Readmission")
    plt.title("Readmission vs Average Time in Hospital")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ####The boxplot shows that patients readmitted within 30 days had the highest median hospital stay at 5 days, compared to 4 days for those readmitted after 30 days and 3 days for those not readmitted.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###Time in Hospital Vs Number of Admissions
    """)
    return


@app.cell
def _(df, plt, sns):
    sns.histplot(data=df, x='time_in_hospital')
    plt.xlabel('Days in Hospital')
    plt.ylabel('Encounters')
    plt.axvline(df["time_in_hospital"].median(), color="red")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ####The histogram shows that most hospital admissions lasted between 1 and 3 days, with the number of admissions decreasing as length of stay increases. Average stay was 4 days.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###Number of Diagnoses vs Time in Hospital
    """)
    return


@app.cell
def _(df, plt, sns):
    sns.lineplot(data=df, x='number_diagnoses', y='time_in_hospital', hue='readmitted')
    plt.xlabel("Number of Diagnoses")
    plt.ylabel("Days in Hospital")
    plt.title("Length of Stay vs Number of Diagnoses and Readmission")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ####The line graph shows that length of stay increases as the number of diagnoses increases across all readmission groups, with patients readmitted within 30 days having a slight increase in diagnoses counts.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###Correlation Coefficient for Number of Diagnoses and Time in Hospital
    """)
    return


@app.cell
def _(df):
    corr = df["number_diagnoses"].corr(df["time_in_hospital"])
    print(f'r = {corr}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ####The correlation coefficient of r = 0.24267560563115376 shows a small positive association
    """)
    return


if __name__ == "__main__":
    app.run()
