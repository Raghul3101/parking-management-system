# from datetime import datetime

# current_datetime = datetime.now()
# formatted_datetime = current_datetime.strftime("%H:%M")
# print(formatted_datetime)
from datetime import datetime

# Get the current time
now = datetime.now()

# Create another datetime object with a different time
other_time = datetime(2023, 11, 9, 12, 0, 0)  # Example: November 9, 2023, 12:00:00

# Calculate the time difference
time_difference = now - other_time

# Calculate minutes and seconds
minutes, seconds = divmod(time_difference.total_seconds(), 60)

print(f"Time difference: {int(minutes)} minutes and {int(seconds)} seconds")