# RiskGame_WinProbability

RiskGame_WinProbability is a Python algoriothim to determine the statistical probability of winning a battle in RISK between a certain number of offensive and defensive troops.

# Usage

## World Domination Mode

A) The game of RISK: World Domination is played in such a way that attacker can roll upto the number of dice they are attacking with (upto 3 dice max in one roll) and the defender can roll upto the number of dice they are defending in their territory (upto 2 dice max in one roll).

B) The highest rolled offensive die is compared to the highest rolled defensive die, and
   1. the attacker loses if the value of the offensive die <= defense dice,
   2. the defender loses if the value of the attack dice > defense dice.

C) The compared dice are discarded, and if both players still have dice remaining, repeat the above steps for a new roll.

## Capital Conquest Mode

A) The game of RISK: Capital Conquest is played in such a way that attacker can roll upto the number of dice they are attacking with (upto 3 dice max in one roll) and the defender can roll upto the number of dice they are defending in their territory (upto 2 dice max in one roll).

B) The highest rolled offensive die is compared to the highest rolled defensive die, and
   1. the attacker loses if the value of the offensive die <= defense dice,
   2. the defender loses if the value of the attack dice > defense dice.

C) The compared dice are discarded, and if both players still have dice remaining, repeat the above steps for a new roll.

# Result
 
The Python algorithm will statistically estimate the number of troops you will have remaining after a battle and if you will win or not.
