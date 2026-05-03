import pandas as pd
import random
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print("Name: Divanshi")
print("URN: 2315056")

df = pd.read_csv("data.csv")

X = df[["Age", "BP", "Cholesterol"]]
y = df["Risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

population_size = 6
generations = 5

population = []

for i in range(population_size):
    individual = {
        "max_depth": random.randint(1, 10),
        "min_samples_split": random.randint(2, 10)
    }
    population.append(individual)

def fitness(individual):
    model = DecisionTreeClassifier(
        max_depth=individual["max_depth"],
        min_samples_split=individual["min_samples_split"]
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)

for generation in range(generations):
    population = sorted(population, key=fitness, reverse=True)

    new_population = population[:2]

    while len(new_population) < population_size:
        parent1 = random.choice(population[:3])
        parent2 = random.choice(population[:3])

        child = {
            "max_depth": random.choice([parent1["max_depth"], parent2["max_depth"]]),
            "min_samples_split": random.choice([parent1["min_samples_split"], parent2["min_samples_split"]])
        }

        if random.random() < 0.2:
            child["max_depth"] = random.randint(1, 10)

        if random.random() < 0.2:
            child["min_samples_split"] = random.randint(2, 10)

        new_population.append(child)

    population = new_population

best_solution = population[0]
best_accuracy = fitness(best_solution)

print("Best Hyperparameters:", best_solution)
print("Best Accuracy:", best_accuracy)