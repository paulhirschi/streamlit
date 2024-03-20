import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns

sns.set_style()

st.title('Palmer\'s Penguins')
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')
# selected_species = st.selectbox(
# 	'What species would you like to visualize?',
# 	['Adelie', 'Gentoo', 'Chinstrap']
# )
penguin_file = st.file_uploader('Select your local Penguins CSV (default provided)')
if penguin_file is not None:
	penguins_df = pd.read_csv(penguin_file)
else:
	penguins_df = pd.read_csv('penguins.csv')
variables = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
selected_x_var = st.selectbox(
	'What do you want the x variable to be?',
	variables
)
selected_y_var = st.selectbox(
	'What about the y?',
	variables
)
selected_sex = st.selectbox(
	'What sex do you want to filter for?',
	['all penguins', 'male penguins', 'female penguins']
)

if selected_sex == 'male penguins':
	penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_sex == 'female penguins':
	penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
	pass

# penguins_df = penguins_df[penguins_df['species'] == selected_species]
markders = {'Adelie': 'X', 'Gentoo': 's', 'Chinstrap': 'o'}
alt_chart = (
	alt.Chart(
		penguins_df,
		title=f'Scatterplot of Palmer\'s Penguins.'
	)
	.mark_circle()
	.encode(
		x=selected_x_var,
		y=selected_y_var,
		color='species'
	)
	.interactive()
)
st.altair_chart(alt_chart, use_container_width=True)
