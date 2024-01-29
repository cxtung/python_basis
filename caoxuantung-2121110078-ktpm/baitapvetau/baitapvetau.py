def check_ticket_type(departure_time):
    # Chuyển đổi giờ xuất phát thành phút để dễ so sánh
    hour, minute = map(int, departure_time.split(':'))
    giokhoihanh = hour * 60 + minute

    # Kiểm tra điều kiện mua vé
    if (giokhoihanh>=23*60+0 and giokhoihanh<=23*60+59)  or (giokhoihanh <4*60+0):
        return "Không hợp lệ"
    elif (giokhoihanh < 9 * 60 + 30) or (giokhoihanh >= 16 * 60 and giokhoihanh <= 19 * 60 + 30):
        return "Vé thường"
    else:
        return "Vé tiết kiệm"

# Test các trường hợp
test_cases = [
    "0:00",   # Không hợp lệ
    "3:00",   # Không hợp lệ
    "3:59",   # Không hợp lệ
    "4:00",   # Vé thường
    "5:30",   # Vé thường
    "9:29",   # Vé thường
    "9:30",   # Vé tiết kiệm
    "12:00",  # Vé tiết kiệm
    "16:00",  # Vé tiết kiệm
    "16:01",  # Vé thường
    "18:00",  # Vé thường
    "19:30",  # Vé thường
    "19:31",  # Vé tiết kiệm
    "21:00",  # Vé tiết kiệm
    "22:59",  # Vé tiết kiệm
    "23:00",  # Không hợp lệ
    "23:59"   # Không hợp lệ
]

for time in test_cases:
    print(f"Xuất phát lúc {time}: {check_ticket_type(time)}")
