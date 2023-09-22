import sys


def convert_to_base_20(num):
    conversion_map = {0: 'A', 1: 'B', 2: 'C', 3: 'D',
                  4: 'E', 5: 'F', 6: 'G', 7: 'H',
                  8: 'I', 9: 'J', 10: 'K', 11: 'L',
                  12: 'M', 13: 'N', 14: 'O', 15: 'P',
                  16: 'Q', 17: 'R', 18: 'S', 19: 'T'}

    base_20 = ""  
    while num != 0:
        base_20 += conversion_map[num % 20]
        num //= 20
    return base_20[::-1]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(convert_to_base_20(int(sys.argv[1])))
