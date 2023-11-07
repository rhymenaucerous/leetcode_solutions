def binary_insert (seats, seatNumber: int) -> None:
    print("##########")
    left = 0
    right = len(seats) - 1
    mid_point = right//2

    if seatNumber > seats[right]:
        seats.append(seatNumber)
        return
    
    if seatNumber < seats[0]:
        seats.insert(0,seatNumber)
        return

    while True:
        if seatNumber > seats[mid_point]:
            
            if seatNumber < seats[mid_point + 1]:
                print(f"insertion on greater than: seatNumber:{seatNumber}, mid_point: {mid_point}")
                print(f"list before: {seats}")
                seats.insert(mid_point + 1, seatNumber)
                print(f"list after: {seats}")
                return
            
            left = mid_point
            mid_point = (right - left)//2 + left


        elif seatNumber < seats[mid_point]:

            if seatNumber > seats[mid_point - 1]:
                print(f"insertion on greater than: seatNumber:{seatNumber}, mid_point: {mid_point}")
                print(f"list before: {seats}")
                seats.insert(mid_point, seatNumber)
                print(f"list after: {seats}")
                return

            right = mid_point
            mid_point = (right - left)//2 + left