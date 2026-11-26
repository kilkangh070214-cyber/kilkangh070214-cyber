def print_gugudan():
    dan = int(input("몇단을 입력할까요? "))
    print(f"--- {dan}단 ---")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")


# 함수 실행
print_gugudan()
