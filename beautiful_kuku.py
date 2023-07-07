def show_kuku3(max_row: int, max_col: int) -> None:
    for i in range(1, max_row + 1):
        for j in range(1, max_col + 1):
            product = i * j

            if product < 10:
                expression = f"{j} x {i} =  {product}"
            else:
                expression = f"{j} x {i} = {product}"

            print(f"{expression} | ", end="")

        print("\n", end="")


def show_kuku3_with_rjust(max_row: int, max_col: int, max_digit: int) -> None:
    for row in range(1, max_row + 1):
        for col in range(1, max_col + 1):
            product = row * col

            padded_product = str(product).rjust(max_digit)
            padded_row = str(row).rjust(max_digit - 1)

            print(f"{col} x {padded_row} = {padded_product} |", end=" ")

        print("\n", end="")


def main():
    max_row = int(input("行数を入力してください: "))
    max_col = int(input("列数を入力してください: "))

    show_kuku3(max_row, max_col)


if __name__ == "__main__":
    main()
