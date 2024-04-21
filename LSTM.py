import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset, random_split
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

file_path = "match_2023-wimbledon-1301.csv"
df = pd.read_csv(file_path)

features = df[['server', 'p1_distance_run', 'p2_distance_run', 'rally_count', 'speed_mph']]
momentum = df['momentum']
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

input_sequence_length = 10
X, y = [], []

for i in range(len(momentum) - input_sequence_length):
    X.append(scaled_features[i:i+input_sequence_length])
    y.append(momentum[i+input_sequence_length])

X = np.array(X)
y = np.array(y)
X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out

input_size = X.shape[2]
hidden_size = 50
output_size = 1

model = LSTMModel(input_size, hidden_size, output_size)

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(dataset, batch_size=32, shuffle=True)

num_epochs = 10
for epoch in range(num_epochs):
    for inputs, targets in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs.squeeze(), targets)
        loss.backward()
        optimizer.step()

with torch.no_grad():
    test_outputs = model(X_test)
    mse = criterion(test_outputs.squeeze(), y_test)
    print(f"Mean Squared Error: {mse.item()}")

new_data = torch.tensor([scaled_features[-input_sequence_length:]], dtype=torch.float32)
predicted_momentum = model(new_data).item()
print(f"Predicted Momentum: {predicted_momentum}")
