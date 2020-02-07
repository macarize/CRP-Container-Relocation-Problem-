# CRP-Container-Relocation-Problem
 
This project is based on Maglić, L., Gulić, M., & Maglić, L. (2019). Optimization of container relocation operations in port container terminals. Transport, 1-11.

1. Introduction
Due to the increase in world container transport in recent years, there is a need to optimize the operations of container transport that occur within a container terminal in order to improve the entire container transport process from the starting location to the defined destination. In order to get access to an individual container that is stored below others, the upper ones have to be relocated. In order to use the existing stacking surfaces within the terminal more rationally and effectively, exceptional efforts are made for solving the relocation problem with an optimization method. In this paper we propose a model based on a GA that resolves the CRP(Container relocation problem) minimizing the total number of container relocations within the bay and thus speeding up container retrieval.

2. Relocation Rules
   - R1
       1.1 a container is located in the stack  
       1.2 there is a free position in the stack considering the maximum stacking height  
       1.3 the priority of the blocking container is higher that the priorities of all the containers that are currently located in the stack  
       ![R1](https://user-images.githubusercontent.com/54901021/74013311-7e0c1380-49cf-11ea-8014-a71de371b80f.PNG)
    - R2
       2.1 relocate the container to the nearest empty stack
       ![R2](https://user-images.githubusercontent.com/54901021/74013312-7ea4aa00-49cf-11ea-9127-51205da096ce.PNG)
    - R3
       3.1 relocate the container to the nearest and the lowest stack
       3.2 there is at least one container located in the stack
       3.3 there is a free position in the stack considering the maximum stacking height
       ![R3](https://user-images.githubusercontent.com/54901021/74013313-7f3d4080-49cf-11ea-8062-5b50b032f640.PNG)
    - R4
       4.1 relocate the container to the nearest stack that is not full to the maximum stacking height
       ![R4](https://user-images.githubusercontent.com/54901021/74013310-7d737d00-49cf-11ea-8bc3-5538bdb237a1.PNG)
3. Flowchart of the model
![flowChart](https://user-images.githubusercontent.com/54901021/74013323-87957b80-49cf-11ea-851c-2dcc049d01c5.PNG)
4. Average relocations
![avgRelocations](https://user-images.githubusercontent.com/54901021/74013326-882e1200-49cf-11ea-82dc-202cb2a1d874.PNG)
5. 6X3(Tiersxstacks) Results of the implementation of this paper 
- Bay satae  
![bay](https://user-images.githubusercontent.com/54901021/74013966-02ab6180-49d1-11ea-97ca-b084c201fbac.PNG)
- Randomly relocated (avg : 7.8 relocations)
![non-GA](https://user-images.githubusercontent.com/54901021/74013320-849a8b00-49cf-11ea-8eb3-1f92899d2de0.png)
- GA used (avg : 6.88 relocations)
![GA](https://user-images.githubusercontent.com/54901021/74012256-24a2e500-49cd-11ea-84c5-c46f48d1643f.png)
  
