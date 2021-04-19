

def calculate_gpa(marks):
    if 60 <= marks <= 65:
        return '2.0'
    elif 66 <= marks <= 70:
        return '2.5'
    elif 71 <= marks <= 75:
        return '3.0'
    elif 76 <= marks <= 80:
        return '3.5'
    elif 81 <= marks <= 84:
        return '3.8'
    elif marks >= 85:
        return '4.0'
    elif marks < 60:
        return 'Fail'
