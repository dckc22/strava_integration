def calculate_pace(distance, time):
    distance = distance
    total_time = time

    if total_time.count(':') == 2:
        hours, minutes, seconds = total_time.split(':')
    else:
        hours = 0
        minutes, seconds = total_time.split(':')

    total_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
    seconds_per_mile = float(total_seconds) / float(distance)

    minutes_per_mile = int(seconds_per_mile / 60)
    seconds_remainder = int(seconds_per_mile - (minutes_per_mile * 60))

    pace = '{:0=2d}:{:0=2d}'.format(minutes_per_mile, seconds_remainder)
    #pace_dt = datetime.strptime(pace, "%M:%S")
    return pace

def seconds_to_duration(n): 

    h = n//3600
    m = (n%3600) // 60
    s = (n%3600)%60
    duration = ('{:0=2d}:{:0=2d}:{:0=2d}'.format(h,m,s))
    return duration