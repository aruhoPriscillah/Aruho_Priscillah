import numpy as np
import random

# Environment setup
road_length = 5
actions = ['left', 'right']

# Q-table initialization
Q = np.zeros((road_length, len(actions)))

# Hyperparameters
episodes = 1000
learning_rate = 0.8
gamma = 0.9
epsilon = 0.3

# Training loop
for episode in range(episodes):
    state = 0

    while state != 4:
        # ε-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action_index = random.randint(0, 1)  # Explore
        else:
            action_index = np.argmax(Q[state])   # Exploit

        # Apply action (0 = left, 1 = right)
        if action_index == 0:
            next_state = max(0, state - 1)
        else:
            next_state = min(road_length - 1, state + 1)

        # Set reward
        reward = 1 if next_state == 4 else -0.1

        # Q-learning update rule
        old_value = Q[state, action_index]
        next_max = np.max(Q[next_state])
        Q[state, action_index] = old_value + learning_rate * (reward + gamma * next_max - old_value)

        # Transition to next state
        state = next_state

# Display the learned Q-table
print("Trained Q-table:")
print(Q)

# Evaluate the learned policy
state = 0
path = [state]

while state != 4:
    action_index = np.argmax(Q[state])
    if action_index == 0:
        state = max(0, state - 1)
    else:
        state = min(road_length - 1, state + 1)
    path.append(state)

print("Learned path to goal:", path)
