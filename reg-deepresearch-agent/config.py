import os
from dataclasses import dataclass


@dataclass
class ResearchConfiguration:
    """Configuration for research-related models and parameters.

    Attributes:
        critic_model (str): Model for evaluation tasks.
        worker_model (str): Model for working/generation tasks.
        max_search_iterations (int): Maximum search iterations allowed.
    """
    plan_model: str = "gemini-2.5-pro"
    critic_model: str = "gemini-2.5-pro"
    worker_model: str = "gemini-2.5-flash"
    report_model: str = "gemini-2.5-pro"
    max_search_iterations: int = 10


config = ResearchConfiguration()