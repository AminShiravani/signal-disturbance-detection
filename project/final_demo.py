import os
import subprocess

EXPERIMENTS = [
    "experiments/exp1_gaussian.py",
    "experiments/exp2_impulse.py",
    "experiments/exp3_amplitude.py",
    "experiments/exp4_phase.py",
    "experiments/exp5_combined.py",
]


def run_experiment(path):
    print("\n" + "=" * 60)
    print(f"Running {path}")
    print("=" * 60 + "\n")

    subprocess.run(["python", path], check=True)


def main():

    print("STARTING SIGNAL DISTORTION ANALYSIS PROJECT\n")

    # Create the output folder (if it doesn't exist)
    os.makedirs("results/figures", exist_ok=True)
    os.makedirs("results/tables", exist_ok=True)
    os.makedirs("results/reports", exist_ok=True)

    # Run all tests
    for exp in EXPERIMENTS:
        run_experiment(exp)

    print("ALL EXPERIMENTS COMPLETED SUCCESSFULLY")
    print("Check results/ folder for outputs")


if __name__ == "__main__":
    main()
