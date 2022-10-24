# Import dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network

# Read dataset
df_interact = pd.read_csv('/Users/kiara/Downloads/python_lessen/relationsss.csv')

# Set header title
st.title('Network Graph Visualization of Drug-Drug Interactions')

# Define selection options and sort alphabetically
inflation_list = ['inflation', 'generation', 'ceo', 'european',
            'usa']
inflation_list.sort()

# Implement multiselect dropdown menu for option selection
selected_word = st.multiselect('Select word(s) to visualize', inflation_list)

# Set info message on initial site load
if len(selected_word) == 0:
   st.text('Please choose at least 1 word to get started')
# Create network graph when user selects >= 1 item

else:
    df_select = df_interact.loc[df_interact['row_1'].isin(selected_word) | \
    df_interact['row_2'].isin(selected_word)]
    df_select = df_select.reset_index(drop=True)

    # Create networkx graph object from pandas dataframe
    G = nx.from_pandas_edgelist(df_select, 'row_1', 'row_2', 'weight')

    # Initiate PyVis network object
    drug_net = Network(height='465px', bgcolor='#222222', font_color='white')

    # Take Networkx graph and translate it to a PyVis graph format
    drug_net.from_nx(G)

    # Generate network with specific layout settings
    drug_net.repulsion(node_distance=420, central_gravity=0.33,
                       spring_length=110, spring_strength=0.10,
                       damping=0.95)

    
    



   