def xor_challenges(challenge, had_club_member):
    xor_result = int(challenge, 2) ^ int(had_club_member, 2)
    formatted_xor_challenge = '{0:b}'.format(xor_result).zfill(len(challenge))
    return str(formatted_xor_challenge)


def calculate_gamma(xor_challenge):
    same = 0
    flipped = 0
    retossed = 0

    for stage in reversed(xor_challenge):
        if stage == '1':
            retossed += 1
        else:
            if retossed % 2 == 0:
                same += 1
            else:
                flipped += 1

    return same - flipped


def approved_club_member(challenge, club):
    for club_member in club:
        xor_challenge = xor_challenges(challenge, club_member)
        gamma = calculate_gamma(xor_challenge)
        if(gamma != 0):
            return False
    
    return True
    
    
def find_had_club_bruteforce_adhoc(puf_length=6, seed=31):
    had_club = []
    num_challenges = 2 ** puf_length
    for num in range(num_challenges):
        challenge = '{0:b}'.format(num + seed).zfill(puf_length)

        if approved_club_member(challenge, had_club):
            had_club.append(challenge)

    return had_club


def plot_anchor_challenge_hist(puf_length=13, seed=0, anchor=0, gamma=-8):
    num_challenges = 2 ** puf_length
    anchor_string = '{0:b}'.format(anchor).zfill(puf_length)



    gammabin = find_gamma_bin(n, gamma)
    clist = []
    print(anchor)
    print(anchor_string)
    for v in gammabin:
        c = find_v(v, anchor_string)
        clist.append(c)
    print(clist)
    for i in range(5):
        glist=one_to_many_gamma_list(clist[i], clist)
    # print(glist)
        hist = list_to_histogram(glist)
        pprint.pprint(hist)



if __name__ == '__main__':
    print(find_had_club_bruteforce_adhoc())
    print(find_zero_gamma_club_bruteforce())
