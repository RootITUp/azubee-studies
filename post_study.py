import pandas as pd
from scipy.stats import ttest_rel

def extract_entries(df: pd.DataFrame, was_trained: bool):
    if was_trained:
        eq = df.where(df.User % 2 != 0)
    else:
        eq = df.where(df.User % 2 == 0)

    return eq[eq["User"].notna()]

def prepare_data():
    data = pd.read_csv("preprocessed/main_study_preprocessed.csv")

    trained = extract_entries(df=data, was_trained=True)["Improvement"].to_numpy()
    not_trained = extract_entries(df=data, was_trained=False)["Improvement"].to_numpy()

    return trained, not_trained


trained_diff, not_trained_diff = prepare_data()

print(trained_diff.mean())
print(not_trained_diff.mean())

# Null hypothesis: trained and untrained improvements are equally distributed
t_test_result = ttest_rel(
    trained_diff,
    not_trained_diff,
    # Alternative: mean of the first is smaller than mean of the second distribution
    alternative='greater'
)

print(t_test_result)

# TtestResult(statistic=1.5381972476555226, pvalue=0.06742065093784343, df=29)
# Konfidenzintervall 90 %
# p-Wert 0,06

# Nullhypothese wird abgelehnt, Alternativhypothese wird angenommen
# Die recommended improvements sind im Schnitt größer als die unrecommended improvements