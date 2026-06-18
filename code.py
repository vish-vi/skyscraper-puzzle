import sys
from itertools import permutations as perms

def check_prefix(prefix, required_count, size):
    current_count = count_visible(prefix)
    if current_count > required_count:
        return False
    remaining = size - len(prefix)
    return current_count + remaining >= required_count

def count_visible(arr):
    max_height = 0
    visible_count = 0
    for height in arr:
        if height > max_height:
            max_height = height
            visible_count += 1
    return visible_count

def matrix(size, top, bottom, left, right):
    numbers = list(range(1, size + 1))
    all_columns = list(perms(numbers))
    column_options = [[] for _ in range(size)]
    
    for col_index in range(size):
        for column in all_columns:
            valid_top = (top[col_index] == 0) or (count_visible(column) == top[col_index])
            valid_bottom = (bottom[col_index] == 0) or (count_visible(column[::-1]) == bottom[col_index])
            if valid_top and valid_bottom:
                column_options[col_index].append(column)
        
        if not column_options[col_index]:
            return None
    
    solution = [[None] * size for _ in range(size)]
    already_used = [set() for _ in range(size)]
    
    def check_matrix(col_index):
        if col_index == size:
            for row_index in range(size):
                current_row = [solution[row_index][j] for j in range(size)]
                if left[row_index] != 0 and count_visible(current_row) != left[row_index]:
                    return False
                if right[row_index] != 0 and count_visible(current_row[::-1]) != right[row_index]:
                    return False
            return True
        
        possible_columns = sorted(
            column_options[col_index],
            key=lambda col: sum(col[row] in already_used[row] for row in range(size))
        )
        
        for column in possible_columns:
            conflict = False
            for row in range(size):
                if column[row] in already_used[row]:
                    conflict = True
                    break
            if conflict:
                continue
            
            valid_column = True
            for row in range(size):
                row_so_far = [solution[row][prev_col] for prev_col in range(col_index)] + [column[row]]
                if not check_prefix(row_so_far, left[row], size):
                    valid_column = False
                    break
            
            if not valid_column:
                continue
            
            for row in range(size):
                solution[row][col_index] = column[row]
                already_used[row].add(column[row])
            
            if check_matrix(col_index + 1):
                return True
            
            for row in range(size):
                already_used[row].remove(column[row])
                solution[row][col_index] = None
        
        return False
    
    return solution if check_matrix(0) else None

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    
    lines = [line.split() for line in data.split('\n')]
    size = int(lines[0][0])
    top = list(map(int, lines[1]))
    bottom = list(map(int, lines[2]))
    left = list(map(int, lines[3]))
    right = list(map(int, lines[4]))
    
    result = matrix(size, top, bottom, left, right)
    if result:
        for row in result:
            print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
