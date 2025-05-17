import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset("tips")

# Streamlit page configuration
st.set_page_config(page_title="Seaborn Plots Explorer", layout="wide")

# Sidebar menu
st.sidebar.title("Choose a Plot")
plot_option = st.sidebar.radio(
    "Select the plot to display:",
    ("Scatter Plot: Total Bill vs Tip", 
     "Box Plot: Total Bill by Day", 
     "Violin Plot: Tip by Smoker Status")
)

# App title
st.title("📊 Seaborn Visualizations on the Tips Dataset")
st.markdown("Use the sidebar to choose which plot to display.")

# Plot rendering
if plot_option == "Scatter Plot: Total Bill vs Tip":
    st.subheader("Scatter Plot: Total Bill vs Tip")
    fig, ax = plt.subplots()
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", style="time", ax=ax)
    ax.set_title("Total Bill vs Tip")
    ax.set_xlabel("Total Bill ($)")
    ax.set_ylabel("Tip ($)")
    st.pyplot(fig)

elif plot_option == "Box Plot: Total Bill by Day":
    st.subheader("Box Plot: Total Bill by Day")
    fig, ax = plt.subplots()
    sns.boxplot(data=tips, x="day", y="total_bill", palette="pastel", ax=ax)
    ax.set_title("Total Bill by Day")
    ax.set_xlabel("Day of the Week")
    ax.set_ylabel("Total Bill ($)")
    st.pyplot(fig)

elif plot_option == "Violin Plot: Tip by Smoker Status":
    st.subheader("Violin Plot: Tip by Smoker Status")
    fig, ax = plt.subplots()
    sns.violinplot(data=tips, x="smoker", y="tip", inner="quartile", palette="muted", ax=ax)
    ax.set_title("Tip by Smoker Status")
    ax.set_xlabel("Smoker")
    ax.set_ylabel("Tip ($)")
    st.pyplot(fig)
