from io import StringIO
import pandas as pd
infile='/Users/sandhyagovindarajan/PycharmProjects/Rosalind /HMM'
with open(infile) as fp:
    lines = fp.read().split('\n--------\n')
    obs_state=lines[0]
    hidden_states=lines[2]
    table=StringIO(lines[4])
    fin_table=pd.read_table(table,sep='\s+')
p=1
for h,obs in zip(hidden_states,obs_state):
    p*=fin_table.loc[h,obs]
print(p)
