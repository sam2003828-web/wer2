"""高能物理分析常用的自訂 function 範例（含 loop / while / if）。"""

from math import sqrt


def print_numbers_with_for(start, end):
    """用 for 迴圈印出 start 到 end（含 end）的整數。"""
    for number in range(start, end + 1):
        print(number)


def sum_until_with_while(limit):
    """用 while 迴圈把 1 累加到 limit，回傳總和。"""
    total = 0
    current = 1

    while current <= limit:
        total += current
        current += 1

    return total


def check_score_with_if(score):
    """用 if / elif / else 判斷分數等級。"""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def find_even_numbers(numbers):
    """搭配 for + if，找出所有偶數並回傳 list。"""
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


# ===== 下面是高能物理分析常用的自訂 function =====

def mean(values):
    """計算平均值。"""
    if not values:
        raise ValueError("values 不能是空的")
    return sum(values) / len(values)


def sample_std(values):
    """計算樣本標準差（N-1）。"""
    if len(values) < 2:
        raise ValueError("至少需要兩筆資料才能算樣本標準差")

    avg = mean(values)
    variance = sum((x - avg) ** 2 for x in values) / (len(values) - 1)
    return sqrt(variance)


def z_scores(values):
    """把一串資料轉成 z-score，常用於快速找 outlier。"""
    std = sample_std(values)
    avg = mean(values)
    return [(x - avg) / std for x in values]


def chi_square(observed, expected):
    """計算 Pearson 卡方值 Σ((obs-exp)^2 / exp)。"""
    if len(observed) != len(expected):
        raise ValueError("observed 與 expected 長度必須一致")

    chi2 = 0.0
    for obs, exp in zip(observed, expected):
        if exp <= 0:
            raise ValueError("expected 的每個值都要 > 0")
        chi2 += (obs - exp) ** 2 / exp
    return chi2


def invariant_mass(px, py, pz, energy):
    """由四動量 (E, px, py, pz) 計算不變質量 m = sqrt(E^2 - |p|^2)。"""
    p2 = px**2 + py**2 + pz**2
    m2 = energy**2 - p2
    return sqrt(max(m2, 0.0))


def transverse_momentum(px, py):
    """計算橫動量 pT = sqrt(px^2 + py^2)。"""
    return sqrt(px**2 + py**2)


def pass_basic_event_selection(event, min_pt=25.0, max_abs_eta=2.4):
    """基本事件篩選：以 if 條件切資料（cut-based analysis）。

    event 需包含：
    - pt: 橫動量
    - eta: 偽快度
    - n_jets: 噴注數量
    """
    if event["pt"] < min_pt:
        return False
    if abs(event["eta"]) > max_abs_eta:
        return False
    if event["n_jets"] < 2:
        return False
    return True


def select_events(events, min_pt=25.0, max_abs_eta=2.4):
    """回傳通過基本 cut 的事件列表。"""
    selected = []
    for event in events:
        if pass_basic_event_selection(event, min_pt=min_pt, max_abs_eta=max_abs_eta):
            selected.append(event)
    return selected


if __name__ == "__main__":
    # 基礎流程控制
    print("for 迴圈範例：")
    print_numbers_with_for(1, 5)

    print("\nwhile 迴圈範例：")
    result = sum_until_with_while(5)
    print(f"1 加到 5 的總和是：{result}")

    print("\nif 判斷範例：")
    grade = check_score_with_if(86)
    print(f"86 分的等級是：{grade}")

    print("\nfor + if 範例：")
    evens = find_even_numbers([1, 2, 3, 4, 5, 6])
    print(f"偶數有：{evens}")

    # 高能物理分析常見範例
    sample = [98.1, 101.5, 99.7, 100.2, 102.3]
    print("\n統計量範例：")
    print("mean:", mean(sample))
    print("std:", sample_std(sample))
    print("z-scores:", z_scores(sample))

    obs = [12, 9, 15, 11]
    exp = [10, 10, 10, 10]
    print("\nchi-square:", chi_square(obs, exp))

    m = invariant_mass(px=30.0, py=40.0, pz=20.0, energy=80.0)
    print("invariant mass:", m)
    print("pT:", transverse_momentum(px=30.0, py=40.0))

    events = [
        {"pt": 22.0, "eta": 1.2, "n_jets": 3},
        {"pt": 45.0, "eta": 2.1, "n_jets": 2},
        {"pt": 60.0, "eta": 2.7, "n_jets": 4},
    ]
    print("selected events:", select_events(events))
