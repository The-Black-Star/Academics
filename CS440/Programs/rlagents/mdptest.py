# CS 440 Reinforcement Learning Assignment
# (C) 2017 Travis Mandel

import mdp
import environments as envs
import sys

# Tests whether planning can recover optimal policies in the two environments
# if they are known
refRSpol = {(5, 9): 1, (4, 7): 1, (1, 3): 1, (4, 8): 1, (5, 6): 1, (2, 8): 0, (0, 7): 0, (0, 0): 1, (1, 6): 0, (3, 7): 1, (2, 5): 1, (0, 3): 1, (5, 8): 1, (1, 2): 1, (4, 9): 0, (5, 5): 1, (2, 9): 0, (4, 4): 1, (1, 5): 1, (3, 6): 1, (0, 4): 1, (3, 3): 1, (1, 1): 1, (0, 1): 1, (2, 6): 1, (4, 5): 1, (2, 2): 1, (1, 4): 1, (3, 9): 0, (0, 5): 0, (1, 9): 0, (0, 8): 0, (3, 5): 1, (2, 7): 0, (4, 6): 1, (5, 7): 1, (0, 2): 1, (3, 8): 0, (0, 6): 0, (1, 8): 0, (1, 7): 0, (0, 9): 0, (2, 3): 1, (3, 4): 1, (2, 4): 1}
refMMpol = {((0, 0), 12): 2, ((1, 0), 12): 1, ((0, 0), 11): 2, ((1, 1), 12): 0, ((2, 0), 12): 2, ((1, 0), 11): 1, ((0, 0), 10): 2, ((1, 2), 12): 0, ((1, 1), 11): 2, ((3, 0), 12): 1, ((2, 0), 11): 2, ((1, 0), 10): 2, ((0, 0), 9): 1, ((2, 2), 12): 0, ((0, 2), 12): 1, ((1, 2), 11): 0, ((1, 1), 10): 0, ((3, 1), 12): 0, ((4, 0), 12): 1, ((3, 0), 11): 1, ((2, 0), 10): 2, ((1, 0), 9): 2, ((0, 0), 8): 1, ((2, 3), 12): 2, ((2, 2), 11): 1, ((0, 3), 12): 0, ((0, 2), 11): 0, ((1, 2), 10): 2, ((1, 1), 9): 1, ((4, 1), 12): 0, ((3, 1), 11): 0, ((4, 0), 11): 1, ((3, 0), 10): 1, ((2, 0), 9): 1, ((1, 0), 8): 1, ((0, 0), 7): 2, ((2, 3), 11): 2, ((2, 2), 10): 1, ((0, 3), 11): 0, ((0, 2), 10): 0, ((1, 2), 9): 2, ((1, 1), 8): 1, ((4, 2), 12): 0, ((4, 1), 11): 0, ((3, 1), 10): 0, ((4, 0), 10): 1, ((3, 0), 9): 1, ((2, 0), 8): 2, ((1, 0), 7): 1, ((0, 0), 6): 2, ((2, 3), 10): 2, ((2, 2), 9): 1, ((0, 3), 10): 0, ((0, 2), 9): 2, ((1, 2), 8): 2, ((1, 1), 7): 1, ((4, 3), 12): 3, ((4, 2), 11): 1, ((4, 1), 10): 1, ((3, 1), 9): 2, ((4, 0), 9): 1, ((3, 0), 8): 1, ((2, 0), 7): 2, ((1, 0), 6): 1, ((0, 0), 5): 2, ((2, 3), 9): 2, ((2, 2), 8): 1, ((0, 3), 9): 0, ((0, 2), 8): 2, ((1, 2), 7): 2, ((1, 1), 6): 1, ((4, 3), 11): 3, ((4, 2), 10): 1, ((4, 1), 9): 1, ((3, 1), 8): 2, ((4, 0), 8): 1, ((3, 0), 7): 1, ((2, 0), 6): 2, ((1, 0), 5): 1, ((0, 0), 4): 2, ((2, 3), 8): 2, ((2, 2), 7): 1, ((0, 3), 8): 0, ((0, 2), 7): 2, ((1, 2), 6): 2, ((1, 1), 5): 1, ((4, 3), 10): 3, ((4, 2), 9): 1, ((4, 1), 8): 1, ((3, 1), 7): 2, ((4, 0), 7): 1, ((3, 0), 6): 1, ((2, 0), 5): 2, ((1, 0), 4): 1, ((0, 0), 3): 2, ((2, 3), 7): 2, ((2, 2), 6): 1, ((0, 3), 7): 0, ((0, 2), 6): 2, ((1, 2), 5): 2, ((1, 1), 4): 1, ((4, 3), 9): 3, ((4, 2), 8): 1, ((4, 1), 7): 1, ((3, 1), 6): 2, ((4, 0), 6): 1, ((3, 0), 5): 1, ((2, 0), 4): 2, ((1, 0), 3): 1, ((0, 0), 2): 2, ((2, 3), 6): 2, ((2, 2), 5): 1, ((0, 3), 6): 0, ((0, 2), 5): 2, ((1, 2), 4): 2, ((1, 1), 3): 1, ((4, 3), 8): 3, ((4, 2), 7): 1, ((4, 1), 6): 1, ((3, 1), 5): 2, ((4, 0), 5): 1, ((3, 0), 4): 1, ((2, 0), 3): 2, ((1, 0), 2): 2, ((0, 0), 1): 2, ((2, 3), 5): 2, ((2, 2), 4): 1, ((0, 3), 5): 0, ((0, 2), 4): 2, ((1, 2), 3): 2, ((1, 1), 2): 1, ((4, 3), 7): 3, ((4, 2), 6): 1, ((4, 1), 5): 1, ((3, 1), 4): 2, ((4, 0), 4): 1, ((3, 0), 3): 1, ((2, 0), 2): 2, ((1, 0), 1): 2, ((0, 0), 0): 2}
rs = envs.RiverswimEnvironment()
rspol = rs.getTrueMDP().computeOptimalPolicy()
for t in range(rs.getTimeHorizon()):
    for s,t1 in refRSpol:
        if t1 != t:
            continue
        if refRSpol[s,t] != rspol[s,t]:
            print("Riverswim policy is incorrect. Optimal action for (s,t) = "+\
            str((s,t)) + " should be " +str(refRSpol[s,t]) + " but is " +\
            str(rspol[s,t]))
            sys.exit(-1)

print("Riverswim policy is correct.")

mm = envs.MazeEnvironment()
mmpol = mm.getTrueMDP().computeOptimalPolicy()
for t in range(mm.getTimeHorizon()):
    for s,t1 in refMMpol:
        if t1 != t:
            continue
        if refMMpol[s,t] != mmpol[s,t]:
            print("Maze policy is incorrect. Optimal action for (s,t) = "+\
            str((s,t)) + " should be " +str(refMMpol[s,t]) + " but is " +\
            str(mmpol[s,t]))
            sys.exit(-1)

print("Maze policy is correct. Done!")
        

