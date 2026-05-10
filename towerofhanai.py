def print_towers(towers):
    print("\nCurrent Towers State:")
    for tower in towers:
        print(f"{tower} = {towers[tower]}")
    print("-" * 40)
def move_disk(source, destination, towers):
    disk = towers[source].pop()
    towers[destination].append(disk)
    print(f"\nMove Disk {disk} from Tower {source} ---> Tower {destination}")
    print_towers(towers)
def tower_of_hanoi(n, source, auxiliary, destination, towers):
    if n == 1:
        move_disk(source, destination, towers)
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary, towers)
    move_disk(source, destination, towers)
    tower_of_hanoi(n - 1, auxiliary, source, destination, towers)
n = int(input("Enter number of disks: "))
num_towers = 3
print(f"\nNumber of Towers Required = {num_towers}")
weights = []
print("\nEnter random disk weights:")
for i in range(n):
    weight = int(input(f"Enter weight of disk {i+1}: "))
    weights.append(weight)
weights.sort(reverse=True)
print("\nDisks arranged from biggest to smallest:")
print(weights)
towers = {
    'A': weights.copy(),  
    'B': [],               
    'C': []                
}
print("\nInitial Towers Arrangement")
print_towers(towers)
print("\n========== STEPS ==========")
tower_of_hanoi(n, 'A', 'B', 'C', towers)
print("\n========== FINAL STATE ==========")
print_towers(towers)