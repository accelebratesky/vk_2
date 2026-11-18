```python
    def connect_over_cost(self):
        for count in range(len(self.costs) - 1):
            if self.costs[count] > 60 and self.costs[count+1] > 60:
                print(f"发现连续高消费：第{count+1}天和第{count+2}天")

```
我真傻，后面才反应过来直接这样写不就行了吗，可能上一题写了状态机这一题还想着吧...