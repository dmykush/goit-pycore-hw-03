from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
   
    upcoming_birthdays = []
    today = datetime.today().date()
    
    # Визначаємо діапазон дат для перевірки (наступні 7 днів включно з сьогодні)
    end_date = today + timedelta(days=7)
    
    for user in users:
        # Конвертуємо дату народження з рядка у datetime об'єкт
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Визначаємо день народження в поточному році
        birthday_this_year = birthday_date.replace(year=today.year)
        
        # Якщо день народження вже минув цього року, розглядаємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_date.replace(year=today.year + 1)
        
        # Перевіряємо, чи день народження потрапляє в наступні 7 днів
        if today <= birthday_this_year <= end_date:
            # Визначаємо дату привітання
            congratulation_date = birthday_this_year
            
            # Перевіряємо, чи день народження припадає на вихідний
            # weekday(): понеділок=0, вівторок=1, ..., субота=5, неділя=6
            if birthday_this_year.weekday() >= 5:  # субота (5) або неділя (6)
                # Переносимо на наступний понеділок
                days_until_monday = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + timedelta(days=days_until_monday)
            
            # Додаємо до списку результатів
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })
    
    return upcoming_birthdays

users = [{'name': 'Dmytro', 'birthday': '1981.06.17'}]

upcoming_birthdays = get_upcoming_birthdays(users)

print(upcoming_birthdays)

