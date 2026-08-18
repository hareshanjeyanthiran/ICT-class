import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1,13)

regular_savings = 500 * months
goal_savings = 700 * months

plt.figure()
plt.plot(
    months,
    regular_savings,
    linestyle="dashed",
    marker="o",
    linewidth=2,
    color="green",
    label="Regular Plan: 500 per month"
)
plt.plot(
    months,
    goal_savings,
    linestyle="solid",
    marker="D",
    linewidth=2,
    color="blue",
    label="Goal Plan: 700 per month"
)
plt.fill_between(
    months,
    regular_savings,
    goal_savings,
    alpha=0.3,
    label="Saving difference",
    color="red"
)
plt.title("Monthly savings progress")
plt.xlabel("Month")
plt.ylabel("Total savings")
plt.xlim(1,12)
plt.ylim(0,9000)
plt.xticks(months)
plt.legend()
plt.show()