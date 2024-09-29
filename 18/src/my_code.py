
#Write functions and define global variables here!
K_point=90

def ask_jump_length():
    return float(input("Length : "))

def ask_style_points():

    style_points = []
    for i in range(5):
        point = float(input(f"Judge {i+1}: "))
        if(0 <= point <= 20 and point % 0.5 == 0):
            style_points.append(point)

    return style_points

def compute_points(length, all_style_points_list):

    all_style_points_list.sort()
    style_points = sum(all_style_points_list[1:4])
    print(style_points)

    return (length-K_point)*1.8 + 60 + style_points

    
if __name__ == "__main__":
    #Write main program below this line
    length = ask_jump_length()
    style_points = ask_style_points()
    total_points = compute_points(length, style_points)
    print(f"{length} {total_points}")

