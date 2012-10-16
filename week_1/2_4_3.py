# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

departure_time_hours = 6 + (52.0/60)
departure_time_minutes = departure_time_hours * 60

easy_pace_minutes = (8 + (15.0/60))
tempo_minutes = (7 + (12.0/60))

arrival_time_minutes = departure_time_minutes + (1 * easy_pace_minutes) + (3 * tempo_minutes) + (1 * easy_pace_minutes)
arrival_time_hours = arrival_time_minutes / 60

print arrival_time_hours	#crudely displays decimal arrival time
