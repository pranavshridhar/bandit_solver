# BANDIT SOLVER

This is a simple project to solve all the levels of OverTheWire's [Bandit](https://overthewire.org/wargames/bandit/) game. 
Every now and then, they are likely to change up the passwords as part of their maintenance routine. It's happened once to me before,
so I decided to create this orchestrator to get all the passwords automatically for me, since there are some levels I am happy to not 
manually have to solve more than once (looking at you, bandit12).

This was also a good opportunity to learn how to write Bash scripts: something I've been wanting to do forever.

**Note**: I've caught this project up to solving until level 25, which is how far I've actually gotten as of writing. I'll be
updating this every now and then until I solve all levels of this game (currently there are 34, though I think they hinted at more coming
later).

---

## SOME TECHNICAL DETAILS
This project consists of a Python orchestrator and a series of Shell scripts, each one made to solve a specific level.
The orchestrator will connect to the user for a level N, using the authentication method obtained from level N-1. It will then 
send the script to be executed on the server, which will obtain the authentication method to level N+1. Think of the Python part as 
the body (or brain) and the Shell part as the limbs.

While this project is made to retrieve the authentication methods to each level, it assumes that the way to solve each level will be exactly
the same. While I've done my best to make sure that this remains as dynamic as possible should certain details change (like port numbers), there are
some other details (filepaths specifically) that I am assuming will stay the same.

---

## WANT TO RUN THIS YOURSELF?
I would highly advise that you check out OverTheWire's bandit (linked above) and play through it yourself before checking out anywhere else
in here further. That said, here's what you gotta do to run this project from your local machine:

### WHAT YOU NEED
- Your computer's operating system should not matter, so long as it satisfies the other requirements.
- Python is an absolute necessity (I'm using Python 3.15). Earlier versions (say around 3.12) should also work, but when in doubt, go for the latest.
- Using virtual environments using the `virtualenv` module is highly recommended, but completely optional. It solves so many problems and is generally
good practice.
To install virtual env, execute the command:
```
pip install virtualenv
```

### SETUP STEPS
1. Clone this repo using HTTP (generally works)
```bash
git clone https://github.com/pranavshridhar/bandit_solver.git
```

then navigate into the project directory:
```
cd bandit_solver
```

2. Set up your virtual environment (optional, but still, highly recommended):
```
python -m venv .venv
.venv\Scripts\activate  # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```
You can always leave your virtual environment by executing: `deactivate`.

3. Run the main script:
```
python main.py
```

4. Profit.


