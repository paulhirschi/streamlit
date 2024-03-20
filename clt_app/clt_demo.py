import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()
st.title('Illustrating the Central Limit Theorem with Streamlit')
st.header('Header stuff')
st.subheader('An App by Paul Hirschi')
st.write((
	'This app simulates a thousand coin flips using the chance of heads input below,'
	'and then samples with replacement from that population and plots the histogram of the'
	'means of the samples in order to illustrate the central limit theorem!'))
st.latex(r'''
	\frac{1}{2}=\theta^2
	''', help='Awesome math stuff with latex.')
st.markdown(r'''
	* Item 1
	* Item 2

	**Bold** thing with some *italic*.
	Some `inline code`.
	''')

perc_heads = st.number_input(label='Chance of Coins Landing on Heads', min_value=0.0, max_value=1.0, value=0.5)
graph_title = st.text_input(label='Graph Title')
binom_dist = np.random.binomial(1, perc_heads, 1_000)
list_of_means = \
	[np.random.choice(binom_dist, 100, replace=True).mean() for _ in range(0, 1_000)]

fig1, ax1 = plt.subplots()
ax1.set_title(graph_title)
ax1 = plt.hist(list_of_means)
st.pyplot(fig1)

# fig2, ax2 = plt.subplots()
# ax2 = plt.hist([1,1,1,1])
# st.pyplot(fig2)
