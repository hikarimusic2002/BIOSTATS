import biostats as bs
import pandas as pd

# ---------------------------------------------------------------

# One-Way ANOVA
data = pd.read_csv("biostats/dataset/penguins.csv")
result = bs.one_way_anova(data, "bill_length_mm", "species")
result2 = bs.one_way_anova(data, "bill_length_mm", "species", 1)
#print(result)

# Two-Way ANOVA
data = pd.read_csv("biostats/dataset/penguins.csv")
result = bs.two_way_anova(data, "bill_length_mm", ["species", "island"])
result2 = bs.two_way_anova(data, "bill_length_mm", ["species", "island"], 1)
#print(result)

# N-Way ANOVA
data = pd.read_csv("biostats/dataset/penguins.csv")
result = bs.n_way_anova(data, "bill_length_mm", ["species", "island", "sex"])
result2 = bs.n_way_anova(data, "bill_length_mm", ["species", "island", "sex"], 1)
#print(result)

# ---------------------------------------------------------------

# One-Way ANCOVA
data = pd.read_csv("biostats/dataset/penguins.csv")
result = bs.one_way_ancova(data, "body_mass_g", "species", "bill_length_mm")
result2 = bs.one_way_ancova(data, "body_mass_g", "species", "bill_length_mm", 1)
#print(result)

# Two-Way ANCOVA
data = pd.read_csv("biostats/dataset/penguins.csv")
result = bs.two_way_ancova(data, "body_mass_g", "species", ["bill_length_mm", "bill_depth_mm"])
result2 = bs.two_way_ancova(data, "body_mass_g", "species", ["bill_length_mm", "bill_depth_mm"], 1)
#print(result)

# N-Way ANCOVA
data = pd.read_csv("biostats/dataset/penguins.csv")
result = bs.two_way_ancova(data, "body_mass_g", "species", ["bill_length_mm", "bill_depth_mm", "flipper_length_mm"])
result2 = bs.two_way_ancova(data, "body_mass_g", "species", ["bill_length_mm", "bill_depth_mm", "flipper_length_mm"], 1)
#print(result)

# ---------------------------------------------------------------

# Linear Regression
data = pd.read_csv("biostats/dataset/penguins.csv")
result = bs.linear_regression(data, "body_mass_g", "bill_length_mm")
result2 = bs.linear_regression(data, "body_mass_g", "bill_length_mm", 1)
#print(result)

# Multiple Regression
data = pd.read_csv("biostats/dataset/penguins.csv")
result = bs.multiple_regression(data, "body_mass_g", ["bill_length_mm", "bill_depth_mm", "flipper_length_mm"])
result2 = bs.multiple_regression(data, "body_mass_g", ["bill_length_mm", "bill_depth_mm", "flipper_length_mm"], 1)
#print(result)

# Logistic Regression
data = pd.read_csv("biostats/dataset/penguins.csv")
result = bs.logistic_regression(data, "species", "Adelie", ["bill_length_mm", "bill_depth_mm", "flipper_length_mm"])
#print(result)

# ---------------------------------------------------------------