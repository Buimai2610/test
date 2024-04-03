def main():
    file_name = 'noidung.txt'

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        print("Các dòng theo thứ tự ngược lại:")
        for line in reversed(lines):
            print(line.strip()) 
    except FileNotFoundError:
        print(f"Tệp '{file_name}' không tồn tại.")
    except Exception as e:
        print(f"Lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()