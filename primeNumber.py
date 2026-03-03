def is_prime(n):
    """
    判斷一個整數是否為質數
    質數是指大於1的自然數，且只能被1和自己整除
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # 檢查從3到sqrt(n)的所有奇數
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def main():
    """主程式"""
    while True:
        try:
            num = int(input("請輸入一個整數 (輸入0終止): "))
            
            if num == 0:
                print("程式已終止")
                break
            
            if is_prime(num):
                print(f"{num} 是質數")
            else:
                print(f"{num} 不是質數")
        
        except ValueError:
            print("錯誤: 請輸入有效的整數")


if __name__ == "__main__":
    main()
