def add_time(start, duration, weekday = None):
    
    week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    start_h, start_min, duration_h, duration_min, meridiano = read_input(start,duration)

    #trabajo en hora militar y después convierto
    if meridiano == "PM":
        start_h += 12

    end_h = start_h + duration_h
    end_min = start_min + duration_min
    if end_min >= 60:
        end_h += int( (start_min + duration_min)/60 )
        end_min = redondea(((start_min + duration_min)/60 - int( (start_min + duration_min)/60 ))*60)
        
    #how many days past
    days_past = int(end_h/24)

    #returning to AM/PM format
    end_h = redondea(((end_h/24) - int((end_h/24)))*24)
    if end_h >= 12:
        if end_h == 12 and end_min == 0:
            end_meridiano = "M"
        else:
            end_meridiano = "PM"
            if end_h > 12:
                end_h = end_h - 12
    else:
        end_meridiano = "AM"
        if end_h == 0: end_h = 12

    # writing output
    new_time = ""
    new_time += str(end_h)
    new_time += ":"
    if len(str(end_min)) == 1:
        new_time += "0" + str(end_min)
    else:
        new_time += str(end_min)
    new_time += " " + end_meridiano

    if weekday:
        iter = 0
        index = None
        for day in week:
            if weekday.casefold() == day.casefold():
                index = iter
            iter += 1
        sorted_week = week[index:] + week[:index]
        new_time += ", " + sorted_week[redondea( ((days_past/7) - int(days_past/7))*7 )]

    if days_past > 0:
        if days_past == 1:
            new_time += " (next day)"
        else:
            new_time += " (" + str(days_past) + " days later)"

    return new_time

def redondea(num):
    if ( num - int(num) ) > 0.5:
        return int(num) + 1
    else: 
        return int(num)

def read_input(start,duration):
    (init, meridiano) = start.split(" ")
    start_h, start_min = init.split(":")
    duration_h, duration_min = duration.split(":")

    start_h = int(start_h)
    start_min = int(start_min)
    duration_h = int(duration_h)
    duration_min = int(duration_min)
    return start_h, start_min, duration_h, duration_min, meridiano