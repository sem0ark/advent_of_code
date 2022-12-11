"""
A:
The Elves take turns writing down the number of Calories contained
by the various meals, snacks, rations, etc. that they've brought with them,
one item per line. Each Elf separates their own inventory
from the previous Elf's inventory (if any) by a blank line.

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

B:
To avoid this unacceptable situation,
the Elves would instead like to know the total Calories carried
by the top three Elves carrying the most Calories.
That way, even if one of those
Elves runs out of snacks, they still have two backups.
"""

def ab():
    with open('in.txt') as f:
        txt = f.read().split('\n\n')
        print(sorted(map(lambda x: -sum(map(int, x.split('\n')))))[-10:])


if __name__ == "__main__":
    ab()
