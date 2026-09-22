score = float(input("Enter your final score to check your academic status: "))

if score >= 7.0:
    print("You passed, congratulations!")
elif score >= 5.0 and score <= 6.9:
    print("You didn't reach the passing grade, but you qualify for a retake exam.")
else:
    print("Failed!")