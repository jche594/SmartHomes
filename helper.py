import datetime as datetime

def get_half_hour_index(time_str):
    """
    Given a time of day in HH:MM format, return the index corresponding to it in the half_hours array.
    """
    try:
        time_obj = datetime.datetime.strptime(time_str, "%I:%M %p")
        index = time_obj.hour * 2 + (1 if time_obj.minute >= 30 else 0)
        return index
    except ValueError:
        raise ValueError("Time format should be in HH:MM AM/PM format")

def get_indices_for_time_range(time_range_str):
    """
    Given a time range in the format 'HH:MM AM/PM to HH:MM AM/PM', return the list of indices corresponding to it.
    """
    start_time_str, end_time_str = time_range_str.split(" - ")
    start_index = get_half_hour_index(start_time_str)
    end_index = get_half_hour_index(end_time_str)

    if start_index <= end_index:
        return list(range(start_index, end_index + 1))
    else:
        return list(range(start_index, 48)) + list(range(0, end_index + 1))

def get_all_indices_for_time_ranges(time_ranges):
    """
    Given an array of time ranges, return a single array of all relevant indices.
    """
    all_indices = []
    for time_range in time_ranges:
        indices = get_indices_for_time_range(time_range)
        all_indices.extend(indices)
    return all_indices

# Examples 
if __name__ == "__main__":
    # get_all_indices_for_time_ranges
    time_ranges = ["9:00 PM - 7:00 AM"]
    all_indices = get_all_indices_for_time_ranges(time_ranges)
    print(f"The indices for the time ranges {time_ranges} are {all_indices}")

    # get_half_hour_index
    time_of_day = "12:00 AM"
    index = get_half_hour_index(time_of_day)
    print(f"The array index for {time_of_day} is {index}")