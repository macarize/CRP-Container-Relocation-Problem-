# CRP-Container-Relocation-Problem
 
This project is based on Maglić, L., Gulić, M., & Maglić, L. (2019). Optimization of container relocation operations in port container terminals. Transport, 1-11.

1. Introduction
Due to the increase in world container transport in recent years, there is a need to optimize the operations of container transport that occur within a container terminal in order to improve the entire container transport process from the starting location to the defined destination

In order to get access to an individual container that is stored below others, the upper ones have to be relocated

In order to use the existing stacking surfaces within the terminal more rationally and effectively, exceptional efforts are made for solving the relocation problem with an optimization method.

In this paper we propose a model based on a GA that resolves the CRP(Container relocation problem) minimizing the total number of container relocations within the bay and thus speeding up container retrieval.

2. Relocation Rules
   - R1
   - a container is located in the stack
   - there is a free position in the stack considering the maximum stacking height
   - the priority of the blocking container is higher that the priorities of all the containers that are currently located in the stack
