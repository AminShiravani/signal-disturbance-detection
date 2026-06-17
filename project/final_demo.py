import os
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXPERIMENTS = [
    "experiments/exp1_gaussian.py",
    "experiments/exp2_impulse.py",
    "experiments/exp3_amplitude.py",
    "experiments/exp4_phase.py",
    "experiments/exp5_combined.py",
]


def run_experiment(path):
    full_path = os.path.join(BASE_DIR, path)

    print("\n" + "=" * 60)
    print(f"Running {path}")
    print("=" * 60 + "\n")

    subprocess.run([sys.executable, full_path], check=True, cwd=BASE_DIR)


def main():
    print("\nSTARTING SIGNAL DISTORTION ANALYSIS PROJECT\n")


    for exp in EXPERIMENTS:
        run_experiment(exp)

    print("\nALL EXPERIMENTS COMPLETED SUCCESSFULLY")
    print("Check results/ folder for outputs\n")


if __name__ == "__main__":
    main()
