#!/usr/bin/python3
import re

input_raw = "".join(open("11/input.txt", "r").readlines())

class Monke():
    def __init__(self, items: list[int], rule: dict[str, str, int, int, int], antiworry=False):
        self.items = items
        self.operator = rule[0]
        self.factor = rule[1]
        self.divisible_by = rule[2]
        self.true = rule[3]
        self.false = rule[4]
        self.inspections = 0
        self.antiworry = antiworry
    
    def add_item(self, prio):
        self.items.append(prio)
    
    def remove_item(self, item):
        self.items.pop(self.items.index(item))
    
    def do_the_math_thing(self, item):
        if self.operator == "+":
            return item + int(self.factor)
        elif "old" in self.factor:
            return item*item
        else:
            return item * int(self.factor)
    def do_turn(self, division_product):
        return_values = []
        for item in self.items:
            self.inspections += 1
            item = self.do_the_math_thing(item)
            if self.antiworry:
                item = item // 3
            else:
                item = item % division_product
            if item % self.divisible_by == 0:
                destination = self.true
            else:
                destination = self.false
            return_values.append({"monkey": destination, "value": item})
        self.items = []
        return(return_values)


    def __repr__(self) -> str:
        return(f"<Monke items='{self.items}' operator='{self.operator}' factor='{self.factor}' true='{self.true}' false='{self.false}' ")


def parse_da_monkes(input, antiworry):
    monkeys = []
    monke_list_raw = input.split("\n\n") # Monkeys are separated by double newline
    monke_list = [l.split("\n") for l in monke_list_raw]
    division_product = 1
    for monkey in monke_list:
        starting_items = [int(x) for x in re.findall(r"(\d+),?",monkey[1])]
        rule = re.search(r"([*+])\s(\d+|old)",monkey[2])
        operator, factor = rule.group(1), rule.group(2)
        divisible_by = int(re.search(r"(\d+)", monkey[3]).group(1))
        division_product *= divisible_by
        true = int(re.search(r"(\d+)", monkey[4]).group(1))
        false = int(re.search(r"(\d+)", monkey[5]).group(1))
        monkeys.append(Monke(starting_items, [operator, factor, divisible_by, true, false], antiworry))
    return(monkeys, division_product)

def do_round(monkeys, division_product):
    for monkey in monkeys:
        todo = monkey.do_turn(division_product)
        for item in todo:
            dest_monkey = item["monkey"]
            value = item["value"]
            monkeys[dest_monkey].add_item(value)
    return monkeys

def calc_monkey_business(rounds, antiworry):
    monkeys, division_product = parse_da_monkes(input_raw, antiworry)
    for i in range(rounds):
        do_round(monkeys, division_product)
    inspections = sorted([m.inspections for m in monkeys])
    result = inspections[-1]*inspections[-2]
    return(result)

print(f"Part 1: {calc_monkey_business(20, True)}")
print(f"Part 2: {calc_monkey_business(10000, False)}")