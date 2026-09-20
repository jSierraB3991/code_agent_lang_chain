from agent import Agent
from libs.methods import stop_model

def main():
    stop_model()
    agent = Agent()
    agent.run_user_input()

if __name__ == "__main__":
    main()

