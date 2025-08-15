'''def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))'''

#HANOI TOWER

'''def hanoi(start, spare, end, n):
    if n == 1:
        print(start + ' -> ' + end)
    else:
        hanoi(start, end, spare, n - 1)
        print(start + ' -> ' + end)
        hanoi(spare, start, end, n - 1)'''

'''def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

# Example: Solve for 3 disks
disks = int(input("Enter the number of disks: "))
tower_of_hanoi(disks, 'A', 'B', 'C')'''

#Alain Hanoi
def move(n: int, src: str, dst: str, helper: str):
    if n == 1:
        print('move disk from peg {} to peg {}'.format(src,dst))
    else:
        move(n-1, src, helper, dst)
        move(1, src, dst, helper)
        move(n-1, helper, dst, src)


def hanoi(n: int):
    move(n, 'A', 'C', 'B')

def main():
    hanoi(2)

if __name__ == '__main__':
    main()