# prisoner

A Python framework exploring a variant of the Iterated Prisoner's Dilemma (IPD) explicitly incorporating survival mechanics through Hit Points (HP).

## Motivation

Traditional Iterated Prisoner's Dilemma (IPD) analyses, such as Axelrod's, ignore survival as an explicit factor. Realistically, survival significantly influences cooperative strategies. This project implements an IPD variant explicitly modeling survival through agents having Hit Points (HP). Each interaction involves payoffs as damage or healing, directly affecting player survival.

## Game Mechanics

Players start with configurable HP.
Payoffs from each interaction translate into HP damage or healing.
Iterations continue until players run out of HP, explicitly modeling survival stakes.
Supports symmetric (equal HP) and asymmetric (unequal HP) setups to explore richer dynamics.

## References

1. **Salagnac, O. & Wakeley, J. (2021)**. [_The Consequences of Switching Strategies in a Two-Player Iterated Survival Game_](https://arxiv.org/abs/2006.06413)  
   Models iterated Prisoner's Dilemma scenarios as survival games using Markov chains. Highlights how incorporating survival probabilities rather than additive payoffs fundamentally alters cooperative dynamics.

2. **Maynard Smith, J. (1982).** *Evolution and the Theory of Games.*  
   A foundational work introducing evolutionary game theory and concepts like Evolutionarily Stable Strategies (ESS), discussing games such as the Hawk-Dove game and exploring conditions under which aggressive or peaceful strategies emerge.

3. **Axelrod, R. (1984).** *The Evolution of Cooperation.*  
   Explores strategies in Iterated Prisoner's Dilemma tournaments, famously demonstrating the success of Tit-for-Tat. Does not explicitly address survival, but forms the basis for analyzing cooperation dynamics.

4. **Rousseau, J.-J. (1755).** *Discourse on Inequality* (introduction of Stag Hunt).  
   Origin of the Stag Hunt allegory, illustrating a cooperation dilemma between collective action for a high-risk, high-reward "stag" versus individual pursuit of lower-risk hares.
