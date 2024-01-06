from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    output_dict = defaultdict(list)
    current_day = date.today()

    if len(users) == 0:
        return output_dict

    for user in users:
        user['birthday'] = user['birthday'].replace(year=current_day.year)

        if current_day >= current_day.replace(month=12, day=31) - timedelta(days=6):

            if user['birthday'] <= current_day.replace(month=1, day=1) + timedelta(days=6):
                user['birthday'] = user['birthday'].replace(year=current_day.year + 1)

        if user['birthday'] >= current_day:
            day_of_week = user['birthday'].weekday()

            if current_day.weekday() != 0:

                if user['birthday'] <= (current_day + timedelta(days=6)):

                    if day_of_week == 0:
                        output_dict['Monday'].append(user['name'])

                    elif day_of_week == 1:
                        output_dict['Tuesday'].append(user['name'])

                    elif day_of_week == 2:
                        output_dict['Wednesday'].append(user['name'])

                    elif day_of_week == 3:
                        output_dict['Thursday'].append(user['name'])

                    elif day_of_week == 4:
                        output_dict['Friday'].append(user['name'])

                    elif day_of_week == 5 or day_of_week == 6:
                        output_dict['Monday'].append(user['name'])

                else:

                    if user['birthday'] <= (current_day + timedelta(days=6)):
                        if user['birthday'] >= (current_day - timedelta(days=2)):
                            day_of_week = user['birthday'].weekday()

                            if day_of_week == 0:
                                output_dict['Monday'].append(user['name'])

                            elif day_of_week == 1:
                                output_dict['Tuesday'].append(user['name'])

                            elif day_of_week == 2:
                                output_dict['Wednesday'].append(user['name'])

                            elif day_of_week == 3:
                                output_dict['Thursday'].append(user['name'])

                            elif day_of_week == 4:
                                output_dict['Friday'].append(user['name'])

                            elif day_of_week == 5 or day_of_week == 6:
                                output_dict['Monday'].append(user['name'])

    return output_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Chak", "birthday": datetime(1974, 12, 31).date()},
        {"name": "Lily", "birthday": datetime(1980, 5, 3).date()},
        {"name": "Jack", "birthday": datetime(1985, 1, 2).date()},
        {"name": "Sam", "birthday": datetime(1968, 1, 8).date()},
        {"name": "Bill2", "birthday": datetime(1955, 1, 5).date()},
        {"name": "Bill3", "birthday": datetime(1955, 12, 30).date()},
        {"name": "Bill4", "birthday": datetime(1955, 1, 2).date()},
        {"name": "Bill6", "birthday": datetime(1955, 12, 31).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
