import random

def determine_winner(user_choice, computer1_choice, computer2_choice):
    
    #تعیین برنده بر اساس گزینه‌های انتخاب شده توسط کاربر و دو کامپیوتر
    if user_choice == computer1_choice == computer2_choice:
        return "equal"
    elif user_choice == "✋":
        if computer1_choice == "🤚" and computer2_choice == "🤚":
            return "you"
        elif computer1_choice == "✋" and computer2_choice == "🤚":
            return "com 1"
        elif computer1_choice == "🤚" and computer2_choice == "✋":
            return "com 2"
    elif user_choice == "🤚":
        if computer1_choice == "✋" and computer2_choice == "✋":
            return "you"
        elif computer1_choice == "🤚" and computer2_choice == "✋":
            return "com 1"
        elif computer1_choice == "✋" and computer2_choice == "🤚":
            return "com 2"

def play_game():
    
    #اجرای بازی پالام، پولوم، پيليش
    user_score = 0
    computer1_score = 0
    computer2_score = 0
    
    for _ in range(5):
        print("new game")
        
        # گزینه کاربر
        user_choice = input("please choice(✋ or 🤚): ")
        
        # گزینه کامپیوترها
        computer1_choice = random.choice(["✋", "🤚"])
        computer2_choice = random.choice(["✋", "🤚"])
        
        print("you : ", user_choice)
        print("com 1 : ", computer1_choice)
        print("com 2 : ", computer2_choice)
        
        winner = determine_winner(user_choice, computer1_choice, computer2_choice)
        print("winner : ", winner)
        print()
        
        # بروزرسانی امتیازات
        if winner == "you":
            user_score += 1
        elif winner == "com 1":
            computer1_score += 1
        elif winner == "com 2":
            computer2_score += 1
    
    # نمایش نتیجه کلی
    print("----- result -----")
    print("your : ", user_score)
    print("com 1 : ", computer1_score)
    print("com 2 : ", computer2_score)
    
    # تعیین برنده کلی
    if user_score > computer1_score and user_score > computer2_score:
        print("The ultimate winner : you")
    elif computer1_score > user_score and computer1_score > computer2_score:
        print("The ultimate winner : com 1")
    elif computer2_score > user_score and computer2_score > computer1_score:
        print("The ultimate winner : com 2")
    else:
        print("equal")


# اجرای بازی
play_game()