class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        num_monsters = len(dist)
        time = []
        for index in range(num_monsters):
            #time is list of time in minutes for each monster reaching the city
            time.append(dist[index]/speed[index])
        
        time = sorted(time)
        monsters_killed = 0

        while monsters_killed < num_monsters:
            if time[0] <= monsters_killed:
                break
            else:
                time.pop(0)
                monsters_killed += 1


        return num_monsters - len(time)