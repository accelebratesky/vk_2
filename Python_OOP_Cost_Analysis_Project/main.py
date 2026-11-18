# -*- coding: utf-8 -*-
"""
校园食堂消费分析（Python 面向对象版）
=====================================
用 class StudentCost 把一个学生的“7 天食堂消费记录”封装成一个对象：
    数据（属性）：name（姓名）、costs（7 天消费金额列表）
    行为（方法）：money / cost_most / cost_least / over_cost /
                 judge_cost / stage_all / connect_over_cost / show_all

运行方式：python main.py
"""


class StudentCost:
    # 等级阈值集中写成类属性，避免在代码里到处散落“魔法数字”
    LOW_LINE = 40
    HIGH_LINE = 60

    # ---------- 构造方法 ----------
    def __init__(self, name, costs):
        self.name = name
        self.costs = costs

    # ---------- 1. 总消费 & 平均消费 ----------
    def money(self):
        all_money = sum(self.costs)
        pinjun_money = all_money / len(self.costs)
        return pinjun_money, all_money

    # ---------- 2. 消费最高的一天 ----------
    def cost_most(self):
        biggest_cost = max(self.costs)
        count = 1
        for cost in self.costs:
            if cost == biggest_cost:
                break
            count += 1
        return biggest_cost, count

    # ---------- 3. 消费最低的一天 ----------
    def cost_least(self):
        min_cost = min(self.costs)
        count = 1
        for cost in self.costs:
            if cost == min_cost:
                break
            count += 1
        return min_cost, count

    # ---------- 4. 超过平均消费的天数 ----------
    def over_cost(self):
        # 直接复用 money() 的结果，不把“求和/求平均”再抄一遍
        pinjun_money, all_money = self.money()
        count = 0
        for cost in self.costs:
            if cost > pinjun_money:
                count += 1
        return count

    # ---------- 5. 判断单日消费等级 ----------
    def judge_cost(self, cost):
        if cost < self.LOW_LINE:
            return "节省"
        elif cost <= self.HIGH_LINE:
            return "正常"
        else:
            return "偏高"

    # ---------- 6. 逐日输出消费等级 ----------
    def stage_all(self):
        count = 1
        for cost in self.costs:
            print(f"第{count}天：{cost:g}元，{self.judge_cost(cost)}")
            count += 1

    # ---------- 7. 找出连续两天都超过 60 元 ----------
    def connect_over_cost(self):
        found = False
        # 只要看相邻两位，用下标 range(len(costs) - 1) 就够了
        for count in range(len(self.costs) - 1):
            if self.costs[count] > self.HIGH_LINE and self.costs[count + 1] > self.HIGH_LINE:
                print(f"发现连续高消费：第{count + 1}天和第{count + 2}天")
                found = True
        if not found:
            print("未发现连续两天消费超过60元")

    # ---------- 8. 一次性输出完整分析报告 ----------
    def show_all(self):
        pinjun_money, all_money = self.money()
        biggest_cost, most_day = self.cost_most()
        min_cost, least_day = self.cost_least()
        print(f"学生：{self.name}")
        print(f"本周总消费：{all_money:g}元")
        print(f"平均每天消费：{pinjun_money:.2f}元")
        print(f"消费最高：第{most_day}天，{biggest_cost:g}元")
        print(f"消费最低：第{least_day}天，{min_cost:g}元")
        print(f"超过平均消费：{self.over_cost()}天")
        self.stage_all()
        self.connect_over_cost()


def main():
    # 学生一：题目给出的示例数据
    student = StudentCost("张三", [42, 35, 48, 58, 61, 63, 39])
    student.show_all()

    print()

    # 学生二：整体更高，有 3 天连续偏高
    student2 = StudentCost("李四", [66, 68, 70, 45, 40, 15, 11])
    student2.show_all()

    print()

    # 学生三：边界测试，40 和 60 都应该算“正常”，并且没有连续高消费
    student3 = StudentCost("王五", [38.5, 40, 60, 61, 39.5, 20, 12])
    student3.show_all()


if __name__ == "__main__":
    main()
