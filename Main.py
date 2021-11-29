from math import factorial

from TacticalVotingRisk import TacticalVotingRisk
from VotingSituation import VotingSituation
from Vot_Scheme import VotingScheme, compute_vot_scheme
import numpy as np
# import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def getOutcome(voters, candidates, scheme_type):
    scheme = compute_vot_scheme(scheme_type, candidates)
    preferencesMatrix = VotingSituation(voters, candidates).voting_matrix

    votes_per_candidate = [0 for i in range(candidates)]

    for voter in range(voters):
        for pref in range(candidates):
            i = preferencesMatrix[pref, voter]
            print(i)
            votes_per_candidate[i - 1] += scheme[pref]

    print(preferencesMatrix[0])
    return votes_per_candidate


# make function to take preferences and voting-scheme, outputs non strategic outcome
# calculate happiness based on non-strategic outcome

def plot_total_tactical_votes_available_per_voter(voters, result):
    # for scheme in VotingScheme:
    #     print(scheme.name)
    #     print(f'How many tactical votes for all voters: {result[scheme.name][1]}')
    #     for voter in range(voters):
    #         print(f'How many tactical votes voter {voter} : {result[scheme.name][1][voter]}')
    #     print("---------------------------------------------------------------------------------------------")

    plot_voters = [str(item) for item in range(1, voters + 1)]

    fig, ax = plt.subplots(1, 4, figsize=(13, 4))

    for scheme in VotingScheme:
        # creating the bar plot
        ax[scheme.value - 1].bar(plot_voters, result[scheme.name][1], color='maroon',
                                 width=0.4)
        # adding x label
        ax[scheme.value - 1].set_xlabel("Voter")
        # Set title
        ax[scheme.value - 1].set_title(scheme.name.replace("_", " "))

    # adding y label
    ax[0].set_ylabel("Total tactical votes available")
    plt.show()


def plot_hapiness_per_scheme(voters, result, scheme):
    fig, ax = plt.subplots(1, 2, figsize=(13, 4))

    plt.style.use('seaborn-deep')
    bins = np.linspace(-2, 4, 30)

    for voter in range(voters):
        if len(result[scheme.name][0][voter]) > 0:
            ax[0].hist(
                result[scheme.name][0][voter][0][TacticalVotingRisk.keys["old_happiness"]], bins,
                label=['voter ' + str(voter)])

    # adding x label
    ax[0].set_xlabel("Happiness Value")
    # Set title
    ax[0].set_title("OLD HAPPINESS : "+scheme.name.replace("_", " "))
    ax[0].legend(loc='upper right')

    for voter in range(voters):
        if len(result[scheme.name][0][voter]) > 0:
            ax[1].hist(
                result[scheme.name][0][voter][0][TacticalVotingRisk.keys["new_happiness"]], bins,
                label=['voter ' + str(voter)])

    # adding x label
    ax[1].set_xlabel("Happiness Value")
    # Set title
    ax[1].set_title("NEW HAPPINESS : "+scheme.name.replace("_", " "))
    ax[1].legend(loc='upper right')

    # adding y label
    ax[0].set_ylabel("Voter in the hapiness level")

    plt.show()

def plot_overall_hapiness_per_scheme(voters, result, scheme):
    fig, ax = plt.subplots(1, 2, figsize=(13, 4))

    plt.style.use('seaborn-deep')
    bins = np.linspace(0, 20, 30)

    for voter in range(voters):
        if len(result[scheme.name][0][voter]) > 0:
            ax[0].hist(
                result[scheme.name][0][voter][0][TacticalVotingRisk.keys["old_overall_happiness"]], bins,
                label=['voter ' + str(voter)])

    # adding x label
    ax[0].set_xlabel("Happiness Value")
    # Set title
    ax[0].set_title("OLD OVERALL HAPPINESS : "+scheme.name.replace("_", " "))
    ax[0].legend(loc='upper right')

    for voter in range(voters):
        if len(result[scheme.name][0][voter]) > 0:
            ax[1].hist(
                result[scheme.name][0][voter][0][TacticalVotingRisk.keys["new_overall_happiness"]], bins,
                label=['voter ' + str(voter)])

    # adding x label
    ax[1].set_xlabel("Happiness Value")
    # Set title
    ax[1].set_title("NEW OVERALL HAPPINESS : "+scheme.name.replace("_", " "))
    ax[1].legend(loc='upper right')

    # adding y label
    ax[0].set_ylabel("Voter in the hapiness level")

    plt.show()


if __name__ == "__main__":
    # Basic TVA
    voters = 10
    candidates = 4
    t = TacticalVotingRisk(voters, candidates)
    result = t.compute_risk()

    plot_total_tactical_votes_available_per_voter(voters, result)

    for scheme in VotingScheme:
        plot_hapiness_per_scheme(voters, result, scheme)

    # for scheme in VotingScheme:
    #     plot_overall_hapiness_per_scheme(voters, result, scheme)
