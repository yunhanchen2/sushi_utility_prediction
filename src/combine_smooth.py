import itertools
import random
import matplotlib.pyplot as plt
from collections import Counter

def load_preferences(filename):
    preferences=[]
    with open(filename, 'r') as f:
        for line in f:
            ranking=list(map(int, line.strip().split()))
            preferences.append(ranking)
    return preferences

def compute_reward(S, preferences):
    total_reward=0
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
    return best_S

def evaluate_rewards_over_sample_sizes(filename, k, sample_sizes, primary_data):
    full_preferences= load_preferences(filename)
    num_of_trials=30
    reward=[]
    
    for trial in range(num_of_trials):
        random.shuffle(full_preferences) 
        trial_rewards=[]
        for sample_size in range(1, sample_sizes + 1):
            sampled= full_preferences[:sample_size]
            best_S= find_best_assortment(sampled, k, 10)
            reward= compute_reward(best_S, primary_data)
            trial_rewards.append(reward)
        reward.append(trial_rewards)

    avg_rewards=[]
    for i in range(sample_sizes):  
        total = 0
        for trial in reward: 
            total += trial[i]       
        average = total / num_trials
        avg_rewards.append(average)
    return avg_rewards



def main():
    filenames = ["gpt4-0-shot.txt","primary.txt","random.txt","gpt3.5-no-shot.txt","gpt3.5-0-shot.txt","gpt3.5-3-shot.txt","gpt4-3-shot.txt","gpt3.5-3-shot-no-history.txt"]
    k = int(input("How many sushi do you want to serve customers? (not more than 10): "))
    max_sample_size = 200

    primary_data = load_preferences("5000_a.txt")

    for filename in filenames:
        rewards= evaluate_rewards_over_sample_sizes(filename, k, max_sample_size, primary_data)
        plt.plot(range(1, max_sample_size + 1), rewards, label=filename)

    plt.xlabel("Sample Size")
    plt.ylabel("Average Reward on Full Dataset")
    plt.title(f"Reward vs. Sample Size (k = {k})")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("comparison_plot.png")
    plt.show()


if __name__ == "__main__":
    main()
