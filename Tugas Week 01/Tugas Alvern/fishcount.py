fish = [1,7,5,14,6,2,11,17,24,8,7,1,21,3.15,14,6,31,27,9,17,21,10,7]

def fix_sensor_issues(fish_data):
    for i in range(1, 23):
        if fish_data[i] == -1:
            average = (fish_data[i - 1] + fish_data[i + 1]) // 2
            fish_data[i] = average

def fish_analysis(fish_data):
    max_fish = max(fish_data)
    min_fish = min(fish_data)
    max_index = fish_data.index(max_fish)
    min_index = fish_data.index(min_fish)

    print("Jumlah ikan terbanyak lewat pada jam", max_index + 1, "dengan jumlah", max_fish, "ikan.")
    print("Jumlah ikan paling sedikit lewat pada jam", min_index + 1, "dengan jumlah", min_fish, "ikan.")
fix_sensor_issues(fish)
fish_analysis(fish)