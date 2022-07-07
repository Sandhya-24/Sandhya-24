infile='/Users/sandhyagovindarajan/PycharmProjects/Rosalind /HMM'
with open(infile) as fp:
    lines=fp.read().split()
    print(lines)
    observed_states=lines[0]
    hidden_states=lines[6]
    hidden_states_alpha=lines[8:10]
    observed_states_alpha=lines[2:5]
    line1=list(map(float,lines[15:18]))
    line2=list(map(float,lines[19:]))
    emission_matrix=[]
    emission_matrix.append(line1)
    emission_matrix.append(line2)

p=1
for i in range(len(observed_states)):
    obs_ind=observed_states_alpha.index(observed_states[i])
    hid_ind=hidden_states_alpha.index(hidden_states[i])
    p*=emission_matrix[hid_ind][obs_ind]
print(p)
