from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.logs = []

    def log_step(self, step_description: str, input_info: str, output_info: str):
        """
        Logs a thinking step for the agent.
        """
        entry = {
            "agent": self.name,
            "step": step_description,
            "input": str(input_info),
            "output": str(output_info)
        }
        self.logs.append(entry)

    @abstractmethod
    def run(self, **kwargs) -> any:
        """
        Executes the agent's logic.
        Args:
            **kwargs: Dynamic arguments required for the specific agent.
        Returns:
            any: The output of the agent.
        """
        pass

    def get_logs(self):
        return self.logs
    
    def clear_logs(self):
        self.logs = []
