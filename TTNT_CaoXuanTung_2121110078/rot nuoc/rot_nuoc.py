def pour_water(source, target, source_capacity, target_capacity, target_amount, steps):
    if target == target_amount:
        steps.append(f"Đã đạt được {target_amount} nước trong bình {target_capacity}")

    if source == 0 or target == target_capacity:
        return

    if source > target_capacity - target:
        amount = target_capacity - target
    else:
        amount = source

    new_source = source - amount
    new_target = target + amount

    steps.append(f"{amount} từ bình {source_capacity} vào bình {target_capacity}")

    pour_water(new_source, new_target, source_capacity, target_capacity, target_amount, steps)

def main():
    a_capacity = int(input("Nhập dung tích bình A: "))
    b_capacity = int(input("Nhập dung tích bình B: "))
    target_amount = int(input("Nhập lượng nước cần đạt được: "))

    if target_amount <= a_capacity:
        pour_from = "A"
        pour_to = "B"
        source_capacity = a_capacity
        target_capacity = b_capacity
    else:
        pour_from = "B"
        pour_to = "A"
        source_capacity = b_capacity
        target_capacity = a_capacity

    steps = []
    pour_water(source_capacity, 0, source_capacity, target_capacity, target_amount, steps)

    print("Các bước thực hiện:")
    for step in steps:
        print(step)

if __name__ == "__main__":
    main()
