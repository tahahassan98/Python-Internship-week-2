# User information
full_name = "Taha Hassan"
age = 20
current_year = 2025
country = "pakistan"
hobby = "photography"
graduation_year = current_year + 4  # Calculated graduation year

# Print profile
print(f"Mini Profile:\n"
      f"Full Name: {full_name}\n"
      f"Age: {age}\n"
      f"Current Year: {current_year}\n"
      f"Country: {country}\n"
      f"Hobby: {hobby}\n"
      f"Expected Graduation Year: {graduation_year}")

# Calculate and print years left
years_left = graduation_year - current_year
print(f"\n{full_name} has {years_left} years left until graduation.")