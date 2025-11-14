#分數計算功能設計
#1.	設計簡單的分數計算器：輸入考試成績，程式自動計算平均分數。
#2.	加入錯誤處理：遇到非數字輸入時，提示「請輸入有效分數」。
#3.	每次修改後，使用 GitHub 進行版本管理，留下註解。
def calculate_average_score():
    scores = []
    print("請輸入考試成績，輸入 'done' 結束輸入：")
    
    while True:
        user_input = input("輸入分數：")
        
        if user_input.lower() == 'done':
            break
        
        try:
            score = float(user_input)
            scores.append(score)
        except ValueError:
            print("請輸入有效分數。")
    
    if scores:
        average_score = sum(scores) / len(scores)
        print(f"平均分數為：{average_score:.2f}")
    else:
        print("沒有輸入任何分數。")
if __name__ == "__main__":
    calculate_average_score()
