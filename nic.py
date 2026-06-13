
import FreeSimpleGUI as FSGUI
def decode_nic_details():
    nic = FSGUI.popup_get_text(
        "Enter your 12-digit National ID number:", 
        title="NIC Decoder",
        button_color="red", 
        background_color="blue", 
        text_color="yellow"
    )
    if nic is None:
        return
        
    nic = nic.strip()
    if len(nic) != 12:
        FSGUI.popup(
            "Please enter a valid 12-digit National ID number.", 
            title="Error",
            button_color="red", 
            background_color="blue", 
            text_color="yellow"
        )
        return
    year = int(nic[0:4])
    day_value = int(nic[4:7])
    
    if day_value > 500:
        gender = "Female"
        days_offset = day_value - 500
    else:
        gender = "Male"
        days_offset = day_value

    is_leap = 0
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap = 1
        
    days_in_months = [31, 28 + is_leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    month_idx = 0
    remaining_days = days_offset
    
    for days_in_month in days_in_months:
        if remaining_days <= days_in_month:
            break
        remaining_days -= days_in_month
        month_idx += 1
        
    day_of_month = remaining_days
    month_numeric = month_idx + 1
    
    str_day = str(day_of_month).zfill(2)
    str_month = str(month_numeric).zfill(2)

    q = day_of_month
    m = month_numeric
    y = year
    if m < 3:
        m += 12
        y -= 1
    k = y % 100
    j = y // 100
    
    weekday_idx = (q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
    weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    birthday = weekdays[weekday_idx]
    result_text = f"Birthdate : {str_day} - {str_month} - {year}\n" \
                f"Birthday  : {birthday}\n" \
                f"Gender    : {gender.lower()}"
    FSGUI.popup(
        result_text, 
        title="NIC Details",
        button_color="red", 
        background_color="blue", 
        text_color="yellow"
    )

if __name__ == "__main__":
    decode_nic_details()