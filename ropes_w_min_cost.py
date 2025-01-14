#Connect Ropes with Minimal Cost
#Find the minimum cost of connecting n ropes into one where the cost of connecting two ropes is the sum of their lengths.
#Input: An array of distinct integers where each integer represents the length of a rope. The cost to connect two ropes is equal to the sum of their lengths.
#Output: A minimum-cost way to connect all ropes into a single one.
#
#Example1.  Consider two ways of connecting four ropes of length 
#10, 5, 21, 3.
#First connect ropes of length 3 and 5 to get a rope of length 8. 
#Then, connect ropes of length 8 and 10 into a rope of length 18.
#Finally, connect ropes of length 18 and 21. 
#The resulting rope-connecting scenario 
#(((3+5)+10)+21) has cost 8+18+39=65.
#
#Example2. 5, 6, 7, 8, 9 has cost 81.
#
#Input format.  The first line contains the number n of ropes. 
#The second line contains integers 
#a1,…,an  where ai is the length of the i-th rope.
#
#Output format.  The minimum cost of connecting the ropes into one.
#
#Constraints.  
#1≤n≤100 and 1≤ai≤10**6, for all 1≤i≤n.	

import heapq

def minimum_cost_to_connect_ropes(ropes):
    heapq.heapify(ropes)
    total_cost = 0
    
    while len(ropes) > 1:
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(ropes, cost)
    
    return total_cost


n = int(input())
ropes = list(map(int, input().split()))

print(minimum_cost_to_connect_ropes(ropes))
