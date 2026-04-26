start_point = int(input("Enter a start number (0-100): "))

if start_point > 100 or start_point < 0:
    print("Validation Error: Please stay between 0 and 100.")
else:
    target_stop = int(input("Enter a stopping point: "))
    
    if target_stop < 0:
        print("Validation Error: Stopping point must be 0 or higher.")
    elif target_stop > start_point:
        print("Logic Error: Stop value cannot be higher than start value.")
    else:
        
        print(f"Commencing countdown from {start_point}...")
        
        while target_stop <= start_point:
            print(start_point)
            start_point -= 1 
        print("Countdown successfully completed.")
