import pandas as pd

def read(file_name) -> bool:
    xls = pd.ExcelFile(file_name)
    sheet_names = xls.sheet_names

    # 存储每个工作表的所有行（每行是一个列表）
    all_sheets_rows = {}

    for sheet_name in sheet_names:
        # 读取当前工作表
        df = pd.read_excel(file_name, sheet_name=sheet_name)
        
        # 将每一行转换为列表
        rows = [row.tolist() for index, row in df.iterrows()]
        
        # 存入字典
        all_sheets_rows[sheet_name] = rows

    # 打印结果
    for sheet_name, data in all_sheets_rows.items():
        print(f"工作表: {sheet_name}")
        for row in data:
            print(row)
        print("-" * 40)

    return True

if __name__ == '__main__':
    print("Info: This is read.py")