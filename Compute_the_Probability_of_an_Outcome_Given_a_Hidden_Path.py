lines = []
infile='/Users/sandhyagovindarajan/PycharmProjects/Rosalind /HMM'
with open(infile) as fp:
    lines=fp.read().split()
    hidden_states=lines[0]
    observed_states=lines[6]
    hidden_states_alpha=[]
    hidden_states_alpha=lines[2:5]
    observed_states_alpha=lines[8:10]
    hidden=list(map(float,lines[15:18]))
    obs=list(map(float,lines[19:]))
    emission_matrix=[]
    emission_matrix.append(hidden)
    emission_matrix.append(obs)
    print(emission_matrix)

p=1
for i in range(len(observed_states)):
    obs_ind=observed_states_alpha.index(observed_states[i])
    hid_ind=hidden_states_alpha.index(hidden_states[i])
    p*=emission_matrix[obs_ind][hid_ind]
print(p)
