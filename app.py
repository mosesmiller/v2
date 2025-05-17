import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset("tips")

# Set Streamlit page config
st.set_page_config(page_title="Seaborn Plots Demo", layout="wide")
st.title("📊 Seaborn Visualizations on the Tips Dataset")
st.markdown("This app shows 3 Seaborn plots using the built-in `tips` dataset.")

# Plot 1: Scatter Plot
st.subheader("1. Scatter Plot: Total Bill vs Tip")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", style="time", ax=ax1)
ax1.set_title("Total Bill vs Tip")
ax1.set_xlabel("Total Bill ($)")
ax1.set_ylabel("Tip ($)")
st.pyplot(fig1)

# Plot 2: Box Plot
st.subheader("2. Box Plot: Total Bill by Day")
fig2, ax2 = plt.subplots()
sns.boxplot(data=tips, x="day", y="total_bill", palette="pastel", ax=ax2)
ax2.set_title("Total Bill by Day")
ax2.set_xlabel("Day of the Week")
ax2.set_ylabel("Total Bill ($)")
st.pyplot(fig2)

# Plot 3: Violin Plot
st.subheader("3. Violin Plot: Tip by Smoker Status")
fig3, ax3 = plt.subplots()
sns.violinplot(data=tips, x="smoker", y="tip", inner="quartile", palette="muted", ax=ax3)
ax3.set_title("Tip by Smoker Status")
ax3.set_xlabel("Smoker")
ax3.set_ylabel("Tip ($)")
st.pyplot(fig3)
