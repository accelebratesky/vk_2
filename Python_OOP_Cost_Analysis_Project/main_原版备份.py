
class StudentCost:
    def __init__(self, name, costs):
        self.name = name
        self.costs = costs
    def money(self):
        all_money=sum(self.costs)
        pinjun_money=all_money/len(self.costs)
        return pinjun_money,all_money
    def cost_most(self):
        biggest_cost=max(self.costs)
        count = 1
        for cost in self.costs:
            if cost==biggest_cost:
                break
            count+=1
        return biggest_cost,count
    def cost_least(self):
        min_cost=min(self.costs)
        count = 1
        for cost in self.costs:
            if cost==min_cost:
                break
            count+=1
        return min_cost,count
    def over_cost(self):
        all_money = sum(self.costs)
        pinjun_money = all_money / len(self.costs)
        count = 0
        for cost in self.costs:
            if cost>pinjun_money:
                count+=1
        return count
    def stage_all(self):
        count = 1
        for cost in self.costs:
            if cost<40:
                print(f"第{count}天，{cost}元，节省")

            elif cost<=60 and cost>=40:
                print(f"第{count}天，{cost}元，正常")

            elif cost>60:
                print(f"第{count}天，{cost}元，偏高")
            count +=1

    def connect_over_cost(self):
        state=0
        count=0
        for cost in self.costs:
            if state==0:
               count+=1
               if cost>60:
                  state=1
            elif state==1:
               if cost>60:
                   print(f"发现连续高消费：第{count}天和第{count+1}天")
                   count+=1
               else:
                   state=0
                   count+=1
student = StudentCost(
    "张三",
    [42, 35, 48, 58, 61, 63, 39,88,22,33,44,65,34,66,67,10]
)
print(f"学生：{student.name}")


pinjun_money,all_money=student.money()
print(f"平均每天消费：{pinjun_money}元 \n本周总消费：{all_money}元")
biggest_cost,count = student.cost_most()
print("biggest_cost:",biggest_cost,"天数：",count)
min_cost,count = student.cost_least()
print("min_cost:",min_cost,"天数：",count)
student_over_cost = student.over_cost()
print("over_cost天数：",student_over_cost)
student.stage_all()

student.connect_over_cost()
print()

student2 = StudentCost(
    "李四",
    [66, 68, 70, 45, 40, 15, 11]
)
print(f"学生：{student2.name}")
pinjun_money2, all_money2 = student2.money()
print(f"平均每天消费：{pinjun_money2}元 \n本周总消费：{all_money2}元")

biggest_cost2, count2 = student2.cost_most()
print("biggest_cost:", biggest_cost2, "天数：", count2)

min_cost2, count2 = student2.cost_least()
print("min_cost:", min_cost2, "天数：", count2)
student_over_cost2 = student2.over_cost()
print("student_over_cost2:",student_over_cost2)
student2.stage_all()
student2.connect_over_cost()
