from utils.selectors import GroupedSelector, Selector

if __name__ == "__main__":
    s = GroupedSelector({
        "G1":["1","2","3","4","5"],
        "G2":["1","2","3","4","5"],
        "G3":["1","2","3","4","5"],
        },
        4
    )

    for _ in range(15):
        print(s.getView())
        s.down()
