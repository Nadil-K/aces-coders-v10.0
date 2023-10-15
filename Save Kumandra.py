# Save Kumandra

def min_time_to_defeat_druuns(p, q, strengths):
        strengths.sort(reverse=True)

        fog_units = 0
        fire_units = 0

        total_time = 0

        for strength in strengths:
            while strength > fog_units and strength > fire_units:
                total_time += 1
                fog_units += p
                fire_units += q

            if strength <= fog_units:
                fog_units -= strength
            else:
                fire_units -= strength

        return total_time
    
t=int(input())

for i in range(t):
    p,q = map(int, input().split())
    n=int(input())
    s=list(map(int,input().split()))
    print(min_time_to_defeat_druuns(p, q, s))