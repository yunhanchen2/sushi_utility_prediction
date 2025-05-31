import itertools
import random
import matplotlib.pyplot as plt
from collections import Counter

def load_preferences(filename):
    preferences = []
    with open(filename, 'r') as f:
        for line in f:
            ranking = list(map(int, line.strip().split()))
            preferences.append(ranking)
    return preferences

def compute_reward(S, preferences):
    total_reward = 0
    for pref in preferences:
        for i, sushi in enumerate(pref):
            if sushi in S:
                total_reward += 10 / (i + 1)
                break  
        else:
            total_reward += 0  
    return total_reward

def find_best_assortment(preferences, k, n):
    best_S = None
    best_reward = -1
    for S in itertools.combinations(range(n), k):
        reward = compute_reward(set(S), preferences)
        if reward > best_reward:
            best_reward = reward
            best_S = set(S)
    return best_S, best_reward

def main():
    filename = input("Enter the filename: ")
    k = int(input("How many sushi do you want to serve customers? (not more than 10): "))
    start = int(input("Enter start value: "))
    end = int(input("Enter end value (inclusive): ")) + 1    
    step = int(input("Enter step size: "))

    sample_sizes = list(range(start, end, step))

    weighted_rewards = []

    for sample_size in sample_sizes:
        print(f"\n=== Sample Size: {sample_size} ===")
        full_preferences = load_preferences(filename)
        num_trials = len(full_preferences) // sample_size
        result_counter = Counter()

        for trial in range(1, num_trials + 1):
            sampled_preferences = random.sample(full_preferences, sample_size)
            best_S, sampled_reward = find_best_assortment(sampled_preferences, k, 10)
            full_reward = compute_reward(best_S, full_preferences)
    
            key = (tuple(sorted(best_S)), round(full_reward, 2))
            result_counter[key] += 1

        print("\n=== Summary of Distinct (S, Reward) Pairs ===")
        weighted_sum = 0
        for (S, reward), count in result_counter.most_common():
            percent = 100 * count / num_trials
            weighted_sum += (count / num_trials) * reward
            print(f"S = {list(S)}, Full Reward = {reward:.2f}, Occurred {count} times({percent:.2f}%)")

        print("\n=== Top 2 Most Frequent Solutions ===")
        top_two = result_counter.most_common(2)
        for idx, ((S, reward), count) in enumerate(top_two, 1):
            percent = 100 * count / num_trials
            print(f"Rank {idx}: S = {list(S)}, Reward = {reward:.2f}, Count = {count}, Percent = {percent:.2f}%")

        print(f"\nWeighted average general reward over all trials: {weighted_sum:.2f}")
        weighted_rewards.append(weighted_sum)

    plt.figure(figsize=(10, 6))
    plt.plot(sample_sizes, weighted_rewards, marker='o')

    threshold = 2
    last_reward = None
    for x, y in zip(sample_sizes, weighted_rewards):
        if last_reward is None or abs(y - last_reward) > threshold:
            plt.text(x, y + 5, f"{y:.1f}", ha='center', fontsize=5)
            last_reward = y

    plt.title("Weighted Avg General Reward vs Sample Size")
    plt.xlabel("Sample Size")
    plt.ylabel("Weighted Avg Reward")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
