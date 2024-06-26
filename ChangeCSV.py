import pandas as pd

# Đọc dữ liệu từ file text
with open("D:/WorkFlowTest/result.txt", 'r') as file:
    lines = file.readlines()

# Tạo danh sách để lưu trữ dữ liệu
data = {'name': [], 'factor': [], 'isSuccess': [],  'RunTime': [], 'Cost': []}
current_entry = {}

# Duyệt qua từng dòng trong file
for line in lines:
    line = line.strip()
    # Nếu dòng không rỗng
    if line:
        # Tách từ và giá trị
        key, value = line.split(': ')
        # Lưu giá trị vào từng cột của mục hiện tại
        if key == 'factor':
            current_entry[key] = str(round(0.005 + 0.005 * float(value), 3))  # Thay đổi giá trị factor
        else:
            current_entry[key] = value
    else:
        # Nếu gặp dòng trống, đó là kết thúc của một mục, thêm vào danh sách dữ liệu
        if current_entry:
            for key in data.keys():
                data[key].append(current_entry.get(key, ''))
            current_entry = {}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Lưu DataFrame vào file Excel
df.to_excel('data-ICPCP.xlsx', index=False)
