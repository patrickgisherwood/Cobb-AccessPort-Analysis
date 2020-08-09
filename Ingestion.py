
import os
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

directory = r'C:\Users\patri\Documents\AccessPort\DataLogs'
filename = r'datalog1.csv'

path = os.path.join(directory, filename)
df = pd.read_csv (path, engine='python')


#fig1 = px.line(df, x = 'Time (sec)', y = 'Calculated Load (g/rev)', title='Calculated Load (g/rev')
#ig1.show()

fig = make_subplots(rows=2, cols=1)

fig.add_trace(
    go.Scatter(df, x='Time (sec)', y='Calculated Load (g/rev)'),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(df, x='Time (sec)', y='Boost (psi)'),
    row=2, col=1
)

#fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")
fig.show()




