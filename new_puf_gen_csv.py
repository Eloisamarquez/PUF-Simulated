import numpy as np
import csv


def gen_vertical_csv(stages=32, mu=10, sigma=0.1):
    with open('arbpuf_old_stage-per-row.csv', 'w', newline='') as csvfile:
        fieldnames = ['stage', 'r_i', 's_i', 't_i', 'u_i', 'delta^0_i', 'delta^1_i']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for stage_number in range(1, stages + 1):
            r = np.random.normal(mu, sigma)
            s = np.random.normal(mu, sigma)
            t = np.random.normal(mu, sigma)
            u = np.random.normal(mu, sigma)
            delta_0 = t - u
            delta_1 = s - r

            row = dict(zip(fieldnames, [stage_number, r, s, t, u, delta_0, delta_1]))
            writer.writerow(row)


def gen_horizontal_csv(stages=32, mu=10, sigma=0.1):
    stage=['stage']
    r=['r']
    s=['s']
    t=['t']
    u=['u']
    delta0=['delta0']
    delta1=['delta1']

    for stage_number in range(1, stages + 1):
        stage.append(stage_number)
        r.append(np.random.normal(mu, sigma))
        s.append(np.random.normal(mu, sigma))
        t.append(np.random.normal(mu, sigma))
        u.append(np.random.normal(mu, sigma))
        delta0.append(t[stage_number] - u[stage_number])
        delta1.append(s[stage_number] - r[stage_number])

    with open('arbpuf.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerows([stage, delta0, delta1, r, s, t, u])


if __name__ == "__main__":
    gen_horizontal_csv()
