


def add_time(start, duration, weekday = None):
    """Calculate time after a given time duration
    
    Arguments are not checked!
    Exceptions are not maintained.

    Parameters
    ----------
    start : str
        start time in a format HH:MM AM/PM
    duration : str
        time duration in a format Hours:Minutes
    weekday : str : optional
        name of a day
    
    Returns
    -------
    str
        new time after the duration in a format HH:MM (num of days), day name

    """
    # Processing parameters
    
    (start_time, start_am) = start.split()
    start_am = True if start_am.lower() == "am" else False
    (start_time_h, start_time_m) = start_time.split(":")
    start_time_h = int(start_time_h)
    start_time_m = int(start_time_m)
    start_time_h24 = start_time_h if start_am else (start_time_h + 12) % 24

    (duration_h, duration_m) = duration.split(":")
    duration_h = int(duration_h)
    duration_m = int(duration_m)

    weekdays = {
        "mon" : {"num": 1, "formal" : "Monday"},
        "tue" : {"num": 2, "formal" : "Tueasday"},
        "wed" : {"num": 3, "formal" : "Wednesday"},
        "thu" : {"num": 4, "formal" : "Thursday"},
        "fri" : {"num": 5, "formal" : "Friday"},
        "sat" : {"num": 6, "formal" : "Saturday"},
        "sun" : {"num": 0, "formal" : "Sunday"}
    }
    weekdays_num2code = {details["num"] : code for code, details in weekdays.items()}
    weekday = weekdays.get(weekday.lower()[0:3], None) if weekday is not None else None

    # Calculating the new time
    
    duration_total_m = duration_h * 60 + duration_m
    calc_time_h = start_time_h24 + (start_time_m + duration_total_m) // 60
    calc_time_m = (start_time_m + duration_total_m) % 60
    calc_time_d = calc_time_h // 24
    calc_time_h = calc_time_h % 24

    calc_time_am = "AM" if calc_time_h < 12 else "PM"
    calc_time_h = (calc_time_h % 12)
    calc_time_h = 12 if calc_time_h == 0 else calc_time_h 

    # Preparing the result str

    if weekday is not None:
        calc_weekday_num = (weekday["num"] + calc_time_d) % 7
        calc_weekday_code = weekdays_num2code[calc_weekday_num]

    if calc_time_d == 1:
        result_days = " (next day)"
    elif calc_time_d > 1:
        result_days = f" ({calc_time_d} days later)"
    else:
        result_days = ""

    result_time = f"{calc_time_h}:{calc_time_m:02} {calc_time_am}"
    result_weekday = f", {weekdays[calc_weekday_code]['formal']}" if weekday is not None else ""
    new_time =  result_time + result_weekday + result_days

    return new_time



if __name__ == "__main__":
    print()
    print(add_time("11:40 AM", "0:25"))
    print(add_time("11:30 AM", "2:32", "Monday"))



