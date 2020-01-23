import numpy as np
import csv

def gen_horizontal_csv(mu, sigma):
    stage=['stage']
    r=['r']
    s=['s']
    t=['t']
    u=['u']
    delta0=['delta0']
    delta1=['delta1']

    for stage_number in range(1, n + 1):
        stage.append(stage_number)
        r.append(np.random.normal(mu, sigma))
        s.append(np.random.normal(mu, sigma))
        t.append(np.random.normal(mu, sigma))
        u.append(np.random.normal(mu, sigma))
        delta0.append(t[stage_number] - u[stage_number])
        delta1.append(s[stage_number] - r[stage_number])

    with open('test.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerows([stage, delta0, delta1, r, s, t, u])


mu, sigma = 10, 0.1 # mean and standard deviation
n = 32
gen_horizontal_csv(mu, sigma)