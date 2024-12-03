from create_grid import *
'''O(n^2)'''
def main():
    user_size = int(input("What size grid would you like? (1-8)\n"))
    user_start = input("which corner would you like to start with? (TL, TR, BL, BR)\n")
    user_stop = int(input("Where in the pattern would you like to stop?\n"))
    grid_size = (user_size, user_size)

    create_grid(user_start, user_stop, grid_size)

if __name__ == "__main__":
    main()
