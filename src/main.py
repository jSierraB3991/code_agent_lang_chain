import sys
from agent import Agent
from libs.methods import stop_model, process_args
from tools.file_system.change_path import change_path_tool

def main():
    args = process_args()
    stop_model(args.model)
    if args.project != ".":
        change_path_tool.invoke(args.project)
    agent = Agent(args.model, args.thread_id)
    agent.run_user_input()

if __name__ == "__main__":
    main()

