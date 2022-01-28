def seconds_difference(time_1, time_2):
    """ (number, number) -&gt; number
    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    &gt;&gt;&gt; seconds_difference(1800.0, 3600.0)
    1800.0
    &gt;&gt;&gt; seconds_difference(3600.0, 1800.0)
    -1800.0
    &gt;&gt;&gt; seconds_difference(1800.0, 2160.0)
    360.0
    &gt;&gt;&gt; seconds_difference(1800.0, 1800.0)
    0.0
    """
    
    return time_2 - time_1

def hours_difference(time_1, time_2):
    """ (number, number) -&gt; float
    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    &gt;&gt;&gt; hours_difference(1800.0, 3600.0)
    0.5
    &gt;&gt;&gt; hours_difference(3600.0, 1800.0)
    -0.5
    &gt;&gt;&gt; hours_difference(1800.0, 2160.0)
    0.1
    &gt;&gt;&gt; hours_difference(1800.0, 1800.0)
    0.0
    """

    return ((time_2 - time_1) / 60) / 60

def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -&gt; float
    Return the total number of hours in the specified number
    of hours, minutes, and seconds.
    Precondition: 0 &lt;= minutes &lt; 60  and  0 &lt;= seconds &lt; 60
    &gt;&gt;&gt; to_float_hours(0, 15, 0)
    0.25
    &gt;&gt;&gt; to_float_hours(2, 45, 9)
    2.7525
    &gt;&gt;&gt; to_float_hours(1, 0, 36)
    1.01
    """

    return hours + (minutes / 60) + (seconds / 60 / 60)

def to_24_hour_clock(hours):
    """ (number) -&gt; number
    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.
    Precondition: hours &gt;= 0
    &gt;&gt;&gt; to_24_hour_clock(24)
    0
    &gt;&gt;&gt; to_24_hour_clock(48)
    0
    &gt;&gt;&gt; to_24_hour_clock(25)
    1
    &gt;&gt;&gt; to_24_hour_clock(4)
    4
    &gt;&gt;&gt; to_24_hour_clock(28.5)
    4.5
    """

    return hours % 24


def get_hours(seconds):
    """ (number) -&gt; number
    Return the number of hours equivelant to seconds.
        
    &gt;&gt;&gt; get_hours(3800)
    1
    &gt;&gt;&gt; get_hours(7600)
    2
    &gt;&gt;&gt; get_hours(2400)
    0
    &gt;&gt;&gt; get_hours(3600)
    1
    """
    
    return to_24_hour_clock(seconds // 3600)


def get_minutes(seconds):
    """ (number) -&gt; number
    Return the remainder of seconds remaining and convert to minutes.
    
    &gt;&gt;&gt; get_minutes(3800)
    3
    &gt;&gt;&gt; get_minutes(7600)
    6
    &gt;&gt;&gt; get_minutes(3600)
    0
    """

    return (seconds % 3600) // 60 


def get_seconds(seconds):
    """ (number) -&gt; number
    Return the remainder of seconds remaining and convert to minutes.
    
    &gt;&gt;&gt; get_seconds(3800)
    20
    &gt;&gt;&gt; get_seconds(7600)
    40
    &gt;&gt;&gt; get_seconds(3600)
    0 
    """

    return (seconds % 3600) % 60 
    def time_to_utc(utc_offset, time):
    """ (number, float) -&gt; float
    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.
    &gt;&gt;&gt; time_to_utc(+0, 12.0)
    12.0
    &gt;&gt;&gt; time_to_utc(+1, 12.0)
    11.0
    &gt;&gt;&gt; time_to_utc(-1, 12.0)
    13.0
    &gt;&gt;&gt; time_to_utc(-11, 18.0)
    5.0
    &gt;&gt;&gt; time_to_utc(-1, 0.0)
    1.0
    &gt;&gt;&gt; time_to_utc(-1, 23.0)
    0.0
    &gt;&gt;&gt; time_to_utc(-1, .5)
    23.5
    """

    return to_24_hour_clock(time - utc_offset)

def time_from_utc(utc_offset, time):
    """ (number, float) -&gt; float
    Return UTC time in time zone utc_offset.
    &gt;&gt;&gt; time_from_utc(+0, 12.0)
    12.0
    &gt;&gt;&gt; time_from_utc(+1, 12.0)
    13.0
    &gt;&gt;&gt; time_from_utc(-1, 12.0)
    11.0
    &gt;&gt;&gt; time_from_utc(+6, 6.0)
    12.0
    &gt;&gt;&gt; time_from_utc(-7, 6.0)
    23.0
    &gt;&gt;&gt; time_from_utc(-1, 0.0)
    23.0
    &gt;&gt;&gt; time_from_utc(-1, 23.0)
    22.0
    &gt;&gt;&gt; time_from_utc(+1, 23.0)
    0.0
    &gt;&gt;&gt; time_to_utc(-1, .5)
    1.5
    """

    return to_24_hour_clock(time + (utc_offset))
